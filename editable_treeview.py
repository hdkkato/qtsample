import sys
from PySide import QtGui, QtCore


class Editor(QtGui.QTextEdit):
    """docstring for Editor"""
    def __init__(self, parent=None):
        super(Editor, self).__init__()


class TreeView(QtGui.QTreeView):
    """docstring for TreeView"""
    def __init__(self):
        super(TreeView, self).__init__()
        self.initTree()


    def initTree(self):
        self.model = QtGui.QStandardItemModel()
        rootItem = QtGui.QStandardItem('Root')
        newrootItem = QtGui.QStandardItem('New Root')
        childItem = QtGui.QStandardItem('Child')

        self.root = self.model.invisibleRootItem()
        self.root.appendRow(rootItem)
        self.root = rootItem
        self.root.appendRow(childItem)
        self.root = childItem # move to children
        self.root = self.model.invisibleRootItem()
        self.root.appendRow(newrootItem)

        self.setModel(self.model)

        self.clicked.connect(self.selected)

    def selected(self, index):
        item = self.model.itemFromIndex(index)
        data = self.model.data(index)
        print(str(index), item)
        print(data)


class MainWindow(QtGui.QWidget):
    """docstring for Main"""
    def __init__(self):
        super(MainWindow, self).__init__()
        layout = QtGui.QVBoxLayout(self)
        self.treeview = TreeView()
        self.editor = Editor()
        splitter = QtGui.QSplitter()
        splitter.addWidget(self.treeview)
        splitter.addWidget(self.editor)
        layout.addWidget(splitter)
        
    def change_editor(self, name):
        pass

def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()