#!/usr/env/bin python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt4 import QtCore, QtGui

class Walker(QtCore.QThread):

    sig_status = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(Walker, self).__init__(parent)
        self.path = ''
        self.stopped = False
        self.mutex = QtCore.QMutex()

    def setup(self, path):
        self.path = path
        self.stopped = False

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True

    def restart(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = False

    def run(self):
        file_num = 0
        for root, dirs, files in os.walk(self.path):
            while self.stopped:
                self.msleep(100)
            file_num += len(files)
            self.sig_status.emit(file_num)
        self.stop()
        self.finished.emit()

class Dialog(QtGui.QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.directory = QtGui.QLineEdit("./")
        self.label = QtGui.QLabel("file num: 0")
        self.search_button = QtGui.QPushButton("&search")
        self.search_button.clicked.connect(self.search_files)
        self.stop_button = QtGui.QPushButton("&stop")
        self.stop_button.clicked.connect(self.stop_search)
        
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.directory)
        hbox.addWidget(self.search_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.setWindowTitle("Asynchronous New-style Signal and Slot Sample")
       
        self.path = None
        self.walker = Walker()
        self.walker.sig_status.connect(self.update_status)
        self.walker.finished.connect(self.finish_search)

    @QtCore.pyqtSlot()
    def search_files(self):
        self.search_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        current_path = str(self.directory.text())
        if not os.access(current_path, os.R_OK):
            return
        if current_path == self.path:
            self.walker.restart()
        else:
            self.path = current_path
            if self.walker.isRunning:
                self.walker.terminate()
                self.walker.wait()
            self.walker.setup(current_path)
            self.walker.start()

    @QtCore.pyqtSlot()
    def stop_search(self):
        self.walker.stop()
        self.search_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    @QtCore.pyqtSlot(int)
    def update_status(self, file_num):
        self.label.setText("file num: %d" % file_num)
    
    @QtCore.pyqtSlot()
    def finish_search(self):
        self.search_button.setEnabled(True)
        self.stop_button.setEnabled(False)

def main():
    app = QtGui.QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()