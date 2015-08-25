# -*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
 
TEXTS = [
    ['abc', 'def', 'ghi'],
    ['abeshi', '!', 'you are shocked.'],
    ['行１', '行２', '行３！'],
    ['ItemModelと', 'ItemSelctionModelの', 'テスト']
]
COLOR_LIST = [
    QtGui.QBrush( QtGui.QColor( 255, 255, 255 ) ),
    QtGui.QBrush( QtGui.QColor( 240, 240, 240 ) )
]
 
 
 
class MyModel( QtGui.QStandardItemModel ):
    def __init__( self, row, column, parent=None ):
        super( MyModel, self ).__init__( row, column, parent )
 
    def addItemInRow( self, *texts ):
        row = self.rowCount()                           # 列数を取得。
        for i in range( len(texts) ):
            # QStandardItemを作成し、StandardItemModelにセットする。
            item = QtGui.QStandardItem()
            item.setText( texts[i] )
            item.setBackground( COLOR_LIST[row%2] )
 
            self.setItem( row, i, item )
 
 
 
class Window( QtGui.QWidget ):
    def __init__( self, parent=None ):
        super( Window, self ).__init__( parent )
        layout = QtGui.QVBoxLayout( self )              # メインレイアウト。
 
        # Standard item model
        self.model    = MyModel( 0, 3, self )
        self.selModel = QtGui.QItemSelectionModel( self.model )
 
        # 画面２分割用スプリッタウィジット。
        splitter = QtGui.QSplitter()
        self.treeview = QtGui.QTreeView( self )         # TreeView
        self.table    = QtGui.QTableView( self )        # Table
 
        # 各種ツリーにItemModelとItemSelectionModelを追加。
        self.treeview.setModel( self.model )
        self.treeview.setSelectionModel( self.selModel )
        self.table.setModel( self.model )
        self.table.setSelectionModel( self.selModel )
 
        # Standard item modelにアイテムを追加。
        for t in TEXTS:
            self.model.addItemInRow( *t )
 
        # TreeViewの設定
        self.treeview.setColumnWidth( 1, 140 )          # １列目の幅を140に調整。
        self.treeview.setSelectionMode(                 # 選択モードをマルチに変更
            QtGui.QAbstractItemView.MultiSelection
        )
 
 
        # スプリッタウィジットにtreeViewとtableWidgetを追加。
        splitter.addWidget( self.treeview )
        splitter.addWidget( self.table )
 
        layout.addWidget( splitter )
 
        # ウィンドウの状態を編集-----------------------------------------------
        self.resize( 800, 240 )                         # ウィンドウのサイズ
        self.setWindowTitle( 'Tree View Sample' )       # ウィンドウタイトル
        # ---------------------------------------------------------------------
 
 
if __name__ == '__main__':
    app = QtGui.QApplication( sys.argv )
 
    # 日本語文字コードを正常表示するための設定。
    QtCore.QTextCodec.setCodecForCStrings( QtCore.QTextCodec.codecForLocale() )
 
    window = Window()
    window.show()
 
    sys.exit(app.exec_())