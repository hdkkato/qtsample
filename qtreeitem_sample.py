# -*- coding: utf-8 -*-
 
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
 
dummydata = [
        {
            "path": "Title A",
            "progress": 7,
            "pass": 2
        }, {
            "path": "Movie B",
            "progress": 18,
            "pass": 2
        }, {
            "path": "Dummy",
            "progress": 35,
            "pass": 2
        }, {
             "path": "HogeHoge",
             "progress": 15,
             "pass": 1
        }
    ]
     
class ProcessTreeView(QtGui.QTreeView):
    def __init__(self):
        super(ProcessTreeView, self).__init__()
         
        self._datamodel = QtGui.QStandardItemModel(0, 3)
        self._datamodel.setHeaderData(0, QtCore.Qt.Horizontal, 'Title')
        self._datamodel.setHeaderData(1, QtCore.Qt.Horizontal, 'Pass')
        self._datamodel.setHeaderData(2, QtCore.Qt.Horizontal, 'Process')
        self.setModel(self._datamodel)
 
        index = 0
        for element in dummydata:
            self._add_item(element, index)
            index = index + 1
 
        self.show()
 
    def _add_item(self, process, n):
        titleitem = QtGui.QStandardItem(process.get('path', u''))
        self._datamodel.setItem(n, 0, titleitem)
        passitem = QtGui.QStandardItem(str(process.get('pass', 0)))
        self._datamodel.setItem(n, 1, passitem)
         
        pbar = QtGui.QProgressBar(self)
        pbar.setValue(process.get('progress', 0))
        index = self._datamodel.index(n, 2, QtCore.QModelIndex())
        self.setIndexWidget(index, pbar)
         
 
class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
         
    def initUI(self):
        self.treeview = ProcessTreeView()
         
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.treeview)
         
        self.setLayout(hbox)
         
        self.setWindowTitle('Tree view test')
        self.show()
 
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()