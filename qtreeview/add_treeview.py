import sys
from PySide import QtGui, QtCore


class Node:
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
    """docstring for TreeModel"""
    def __init__(self, parent=None):
        super(TreeModel, self).__init__()
        self.root = Node(['Tree'])
        self.setupTree(self.root)

    def setupTree(self, node):
        # first class
        current = node.addChild(['Root'])
        # second class
        current = current.addChild(['Node'])
        #third class
        current.addChild(['Leaf'])

    # implement virtual method of QAbstractItemModel
    def columnCount(self, parent):
        if parent.isValid():
          # parent.internalPointer()でNodeクラスインスタンスにアクセスする
          return len(parent.internalPointer().data)
        else:
          # header
          return len(self.root.data)

    def rowCount(self, parent):
        if parent.column() > 0:
          return 0

        if not parent.isValid():
          parentItem = self.root
        else:
          parentItem = parent.internalPointer()

        return len(parentItem.children)

    def parent(self, index):
        if not index.isValid():
          return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == self.root:
          return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

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

    def data(self, index, role):
        if not index.isValid():
          return None

        if role != QtCore.Qt.DisplayRole:
          return None

        return index.internalPointer().data[index.column()]


class Main(QtGui.QMainWindow):
    """docstring for Main"""
    def __init__(self, parent=None):
        super(Main, self).__init__()
        self.tree = QtGui.QTreeView(self)
        self.model = TreeModel(self)
        self.selModel = QtGui.QItemSelectionModel(self.model)
        self.selModel.setEditable(True)


        self.tree.setModel(self.model)
        self.tree.setSelectionModel(self.selModel)
        self.setCentralWidget(self.tree)

        # implement shortcut key action
        new_action = QtGui.QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        new_action.triggered.connect(self.addTree)


        # connect to action
        menu = self.menuBar()
        filemenu = menu.addMenu('&File')
        filemenu.addAction(new_action)


    def addTree(self):
        #self.model.root.children[0].addChild(['New Node']).addChild(['New Leaf'])
        self.model.root.addChild(['New Root']).addChild(['New Node']).addChild(['New Leaf'])
        #print(len(self.model.root.children))
        self.model.reset()


def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()