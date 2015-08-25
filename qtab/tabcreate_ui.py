# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabcreate.ui'
#
# Created: Thu Jul  9 15:28:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "GroupBox", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "Radio1", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Radio2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "New Tab", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Tab 1", None, QtGui.QApplication.UnicodeUTF8))

