import sys
from PySide import QtCore, QtGui
from tabcreate_ui import Ui_MainWindow


class NewTab(QtGui.QWidget):
    """docstring for NewTab"""
    def __init__(self):
        super(NewTab, self).__init__()


        

class MainWindow(Ui_MainWindow, QtGui.QMainWindow):
    """docstring for MainWindow"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.create_new_tab)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)


    def create_new_tab(self):
        self.tabWidget.addTab(NewTab(), 'New Tab')

    def close_tab(self, index):
        self.tabWidget.removeTab(index)


def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()