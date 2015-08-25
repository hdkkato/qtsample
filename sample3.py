# -*- coding: utf-8 -*-
 
import sys
import time
 
from PySide           import QtGui,QtCore
from PySide.QtUiTools import QUiLoader

def getWidget(path,load):
    
    qLoader = QUiLoader()
    qFile   = QtCore.QFile(path)
    qFile.open(QtCore.QFile.ReadOnly)
    ui = qLoader.load(qFile,load)
    qFile.close()
    return ui

class TextEdit(QtGui.QWidget):
    
    uiFile  = "textUI.ui"
    count   = 0
    maxLine = 10
    
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.ui = getWidget(self.uiFile,self)

        layout  = QtGui.QVBoxLayout()
        layout.addWidget(self.ui)

        self.setLayout(layout)

        #Signal
        self.ui.pushButton.clicked.connect(self.pushBtn)

        self.p = TestProcess()
        self.p.printThread.connect(self.push)

        self.logModel = QtGui.QStringListModel()
        self.ui.logView.setModel(self.logModel)

    def pushBtn(self):

        self.p.start()

    def push(self,line):

        logs = self.logModel.stringList()
        logs.append(line)
        if len(logs) > self.maxLine:
            logs.pop(0)
        self.logModel.setStringList(logs)
        self.ui.logView.scrollToBottom()


class TestProcess(QtCore.QThread):

    printThread = QtCore.Signal( str )

    def __init__(self,parent=None):
        QtCore.QThread.__init__(self,parent)

    def run(self):

        for i in range(100):
            self.printLog(str(i))
            time.sleep(1)

        self.finished.emit()

    def printLog(self,line):
        
        self.printThread.emit(line)
        

app = QtGui.QApplication(sys.argv)
dlg = TextEdit()
dlg.show()
sys.exit(app.exec_())