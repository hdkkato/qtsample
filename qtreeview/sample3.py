#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

class MyWidget(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    splitter = QtGui.QSplitter(self)
    model=QtGui.QDirModel(self)
    # pane1
    treeview = QtGui.QTreeView()
    treeview.setModel(model)
    treeview.setRootIndex(model.index(QtCore.QDir.currentPath()))
    splitter.addWidget(treeview)
    # pane2
    listview = QtGui.QListView()
    listview.setModel(model)
    listview.setRootIndex(model.index(QtCore.QDir.currentPath()))
    splitter.addWidget(listview)

    self.setCentralWidget(splitter)

if __name__=="__main__":
  app = QtGui.QApplication(sys.argv)
  widget = MyWidget()
  widget.show()
  sys.exit(app.exec_())