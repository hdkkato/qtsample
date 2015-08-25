import sys
from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *

from treeview_ui import Ui_MainWindow


class Node(object):
    """docstring for Node"""
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def addChild(self, data):
        node = Node(data, self)
        self.children.append(node)
        return node

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        else:
            return 0        


class TreeModel(QtCore.QAbstractItemModel):
    """docstring for NewTree"""
    def __init__(self, parent=None):
        super(TreeModel, self).__init__()
        self.root = Node(['Tree'])
        self.setupTree(self.root)

    def setupTree(self, node):
        current = node.addChild(['root'])
        current = current.addChild(['node'])
        current.addChild(['leaf'])

    def addTree(self, node):
        self.root.addChild(node)

    # implement virtual method of QAbstractItemModel
    def columnCount(self, parent):
        if parent.isValid():
            return len(parent.internalPointer().data)
        else:
            return len(self.root.data)

    def rowCount(self, parent):
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parentItem = self.root
        else:
            parentItem = parent.internalPointer()
        return len(parentItem.children)

    def index(self, row, column, parent):
        if row < 0 or column < 0 or row >= self.rowCount(parent) or column >= self.columnCount(parent):
          return QtCore.QModelIndex()

        if not parent.isValid():
          parentItem = self.root
        else:
          parentItem = parent.internalPointer()

        childItem = parentItem.children[row]
        if childItem:
          return self.createIndex(row, column, childItem)
        else:
          return QtCore.QModelIndex()

    def parent(self, index):
        if not index.isValid():
          return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == self.root:
          return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def data(self, index, role):
        if not index.isValid():
          return None

        if role != QtCore.Qt.DisplayRole:
          return None

        return index.internalPointer().data[index.column()]


    def setData(self, index, value, role = Qt.EditRole):
            # You might be expecting Qt.DisplayRole here, but no.
            # Qt.DisplayRole is the *displayed* value of an item, like, a formatted currency value: "$44.00"
            # Qt.EditRole is the raw data of an item, e.g. "4400" (as in cents).
        if role == Qt.EditRole:
            # set the data.
            # the str() cast here is mostly for peace of mind, you can't perform some operations
            # in python with Qt types, like pickling.
            self._items[index.row()] = str(value)

            # *always* emit the dataChanged() signal after changing any data inside the model.
            # this is so e.g. the different views know they need to do things with it.
            #
            # don't be lazy and pass a huge range of values to this, because it is processing-heavy.
            #
            # because we are a simple list, we only have one index to worry about for topleft/bottom right,
            # so just reuse the index we are passed.
            QObject.emit(self, SIGNAL("dataChanged(const QModelIndex&, const QModelIndex &)"), index, index)
            return True
            # unhandled change.
        return False


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """docstring for MainWindow"""
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.model = TreeModel()
        self.treeView.setModel(self.model)

        menu = self.menuBar()

        new_action = QtGui.QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.create_child_tree)

        filemenu = menu.addMenu('&File')
        filemenu.addAction(new_action)
        

    def create_child_tree(self):
        self.model.addTree(['new leaf'])
        self.treeView.reset()



def main():
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()