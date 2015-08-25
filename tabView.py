import sys
from PyQt4 import QtCore, QtGui

class TreeView(QtGui.QTreeView):
    def __init__(self, parent=None):
        super(TreeView, self).__init__(parent)
        model = QtGui.QStandardItemModel()
        item = QtGui.QStandardItem('Model')
        item.setEditable(True)
        child = QtGui.QStandardItem('Inst-1')
        child.setEditable(False)
        item.appendRow(child)
        item2 = child
        for i in range(5):
            child = QtGui.QStandardItem('part-'+str(i+1))
            child.setEditable(False)
            item2.appendRow(child)
        model.setItem(0, 0, item)
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem('Model Tree'))
        self.setModel(model)

class MyWidget(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        tree = TreeView(self)
        self.setCentralWidget(tree)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())