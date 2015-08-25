#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class Node:
  def __init__(self, data, parent=None):
    self.data=data
    self.parent=parent
    self.children=[]

  def addChild(self, data):
    node=Node(data, self)
    self.children.append(node)
    return node

  def row(self):
    if self.parent:
      return self.parent.children.index(self)
    else:
      return 0

class MyModel(QtCore.QAbstractItemModel):
  def __init__(self, parent=None):
    QtCore.QAbstractItemModel.__init__(self, parent)
    # rootノード(表示される最上位のもうひとつ上の階層になる)
    self.root=Node([QtCore.QVariant("Title")]) 
    self.setupTree(self.root)

  def setupTree(self, node):
    # 1階層
    current=node.addChild([self.trUtf8("日本")])
    # 2階層
    current=current.addChild([self.trUtf8("関東")])
    # 3階層
    current.addChild([self.trUtf8("茨城県")])
    current.addChild([self.trUtf8("栃木県")])
    current.addChild([self.trUtf8("群馬県")])
    current.addChild([self.trUtf8("埼玉県")])
    current.addChild([self.trUtf8("千葉県")])
    current.addChild([self.trUtf8("東京都")])
    current.addChild([self.trUtf8("神奈川県")])

  def columnCount(self, parent):
    if parent.isValid():
      # parent.internalPointer()でNodeクラスインスタンスにアクセスする
      return len(parent.internalPointer().data)
    else:
      # header
      return len(self.root.data)

  def data(self, index, role):
    if not index.isValid():
      return QtCore.QVariant()

    if role != QtCore.Qt.DisplayRole:
      return QtCore.QVariant()

    return QtCore.QVariant(index.internalPointer().data[index.column()])

  def flags(self, index):
    if not index.isValid():
      return QtCore.Qt.ItemIsEnabled

    return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

  def headerData(self, section, orientation, role):
    if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
      return self.root.data[section]

    return QtCore.QVariant()

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

  def rowCount(self, parent):
    if parent.column() > 0:
      return 0

    if not parent.isValid():
      parentItem = self.root
    else:
      parentItem = parent.internalPointer()

    return len(parentItem.children)


class MyWidget(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    tree = QtGui.QTreeView(self)
    model=MyModel(self)
    tree.setModel(model)
    self.setCentralWidget(tree)

if __name__=="__main__":
  app = QtGui.QApplication(sys.argv)
  widget = MyWidget()
  widget.show()
  sys.exit(app.exec_())