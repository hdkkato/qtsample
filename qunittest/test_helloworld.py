#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import unittest

from PySide import QtCore, QtGui, QtTest

import helloworld


class TestQHelloWorld(unittest.TestCase):
    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        self.widget = helloworld.QHelloWorld()

    def test_button_clicked(self):
        # 初期状態では text (lineedit) は空白
        self.assertEqual(self.widget.text, u"")
        self.assertEqual(self.widget.lineedit.text(), u"")

        # button の左クリックイベントを発生させる
        QtTest.QTest.mouseClick(self.widget.button, QtCore.Qt.LeftButton)

        # text lineedit が "Hello world" になる
        self.assertEqual(self.widget.text, u"Hello world")
        self.assertEqual(self.widget.lineedit.text(), u"Hello world")


if __name__ == "__main__":
    unittest.main()