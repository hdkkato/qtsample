import sys
from PyQt4 import QtCore
from PyQt4 import QtGui

class Worker(QtCore.QThread):

    mutex = QtCore.QMutex()

    def __init__(self, name = "", parent = None):
        
        QtCore.QThread.__init__(self, parent)
        self.name = name
        self.isStopped = False
        
    def run(self):
        while not self.isStopped:
            ###if not self.mutex.tryLock():
            ###    print self.name + "failed lock"
            ###    continue
            ##with QtCore.QMutexLocker( self.mutex ):
            self.mutex.lock()
            self.print_()
            self.msleep(100)
            self.mutex.unlock()
            
    def print_(self):
        print(self.name, " : execution")
        
        
class Window(QtGui.QWidget):

    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        # threads        
        self.w1 = Worker(name="thread1")
        self.w1.started.connect(self.thread_start)
        self.w1.finished.connect(self.thread_finish)
        self.w1.finished.connect(self.thread_terminated)
        self.w2 = Worker(name="thread2")
        self.w2.started.connect(self.thread_start)
        self.w2.finished.connect(self.thread_finish)
        self.w2.finished.connect(self.thread_terminated)
        # components
        start = QtGui.QPushButton("start", self)
        start.clicked.connect(self.start)
        stop = QtGui.QPushButton("stop", self)
        stop.clicked.connect(self.stop)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(start)
        hbox.addWidget(stop)
        self.setLayout(hbox)

    def start(self):
        self.w1.isStopped = False
        self.w2.isStopped = False
        self.w1.start()
        self.w2.start()
        # It can set priority
        #self.w1.setPriority(QtCore.QThread.LowestPriority)
        #self.w2.setPriority(QtCore.QThread.HighestPriority)
       
    def stop(self):
        self.w1.isStopped = True
        self.w2.isStopped = True
        self.w1.wait()
        self.w2.wait()
        
    def thread_start(self):     print(self.sender().name + "started")
    def thread_finish(self):     print(self.sender().name + "finish")
    def thread_terminated(self):     print(self.sender().name + "terminated")
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()