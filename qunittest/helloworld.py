#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui


class QHelloWorld(QtGui.QWidget):
    u"""サンプルウィジェット"""

    # テキストが変更された際の signal
    text_changed = QtCore.Signal()

    def __init__(self, *args, **kwargs):
        """Create QHelloWorld isntance"""

        super(QHelloWorld, self).__init__(*args, **kwargs)

        self.setup_ui()
        self.setup_events()

    def setup_ui(self):
        u"""UI の設定"""

        # このウィジェットのレイアウトを設定 (縦配列)
        base_layout = QtGui.QVBoxLayout(self)
        base_layout.setObjectName('base_layout')

        # テキストボックス (子ウィジェット) を base_layout に追加
        self.lineedit = QtGui.QLineEdit(parent=self)
        self.lineedit.setObjectName('lineedit')
        base_layout.addWidget(self.lineedit)

        # ボタン (子ウィジェット) を base_layout に追加
        self.button = QtGui.QPushButton(self.tr("&Say"), parent=self)
        self.button.setObjectName('button')
        base_layout.addWidget(self.button)

    def setup_events(self):
        u"""イベントの設定"""

        # 子ウィジェットの signal を再帰的に slot として受け付ける
        # この動作には setObjectName でオブジェクト名がセットされている必要がある
        # これにより
        # def on_<object name>_<signal name>(<signal parameters>) で slot を受け付けることができる
        # 参照: http://www.pyside.org/docs/pyside/PySide/QtCore/QMetaObject.html#PySide.QtCore.PySide.QtCore.QMetaObject.connectSlotsByName
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_text(self):
        return self.lineedit.text()

    def set_text(self, text):
        self.lineedit.setText(text)

    # Qt 版 property 。notify で setter 時の signal をセットできる
    text = QtCore.Property(unicode, get_text, set_text, notify=text_changed)

    @QtCore.Slot()
    def on_button_clicked(self):
        self.text = u"Hello world"


def main():
    import sys

    app = QtGui.QApplication(sys.argv)
    widget = QHelloWorld()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()