# -*- coding:utf-8 -*-
 
import sys
from PyQt4 import QtGui, QtCore
 
# /////////////////////////////////////////////////////////////////////////////
# クリック時に予めセットした文字列をシグナルとして送るボタン。               //
# /////////////////////////////////////////////////////////////////////////////
class MyPushButton( QtGui.QPushButton ):
 
    clickedWithText = QtCore.pyqtSignal( str )  # シグナル
     
    def __init__( self, *arglist, **argdict ):
        super( MyPushButton, self ).__init__( *arglist, **argdict )
 
        # ボタンクリック時に↑で定義したシグナルに信号を送るために
        # clickedシグナルにコネクトする。
        self.clicked.connect( self.emitWithText )
 
    def emitWithText( self ):
        # クリック時にclickWithTextシグナルにエミットするための中間メソッド。 
        self.clickedWithText.emit( self.text() )
# /////////////////////////////////////////////////////////////////////////////
#                                                                            //
# /////////////////////////////////////////////////////////////////////////////
 
 
 
class MainWindow( QtGui.QWidget ):
    def __init__( self, parent=None ):
        super( MainWindow, self ).__init__( parent )
        self.resize( 420, 80 )
        self.setWindowTitle( 'Signal Exsample' )
 
        layout = QtGui.QGridLayout( self )
         
        # カスタムボタンを作成。-----------------------------------------------
        button1 = MyPushButton( 'Alphabet' )
        button1.clickedWithText.connect( self.output )
 
        button2 = MyPushButton( 'Number' )
        button2.clickedWithText.connect( self.output )
 
        button3 = MyPushButton( 'Hoge' )
        button3.clickedWithText.connect( self.output )
        # ---------------------------------------------------------------------
         
        self.resultText = QtGui.QLineEdit( '' )
        self.resultText.setReadOnly( True )
 
        layout.addWidget( button1, 1, 1, 1, 1 )
        layout.addWidget( button2, 1, 2, 1, 1 )
        layout.addWidget( button3, 1, 3, 1, 1 )
        layout.addWidget( self.resultText, 2, 1, 1, 3 )
        layout.setRowStretch( 3, 1 )
 
    def output( self, text ):
        self.resultText.setText( text )
 
if __name__ == '__main__':
    app    = QtGui.QApplication( sys.argv )
    window = MainWindow()
    window.show()
     
    sys.exit( app.exec_() )