import sys
import time

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

class MyThread(QThread):
    def __init__(self):
        super().__init__()
        
    def run(self):
        for i in range(10):
            print("this mythread is ui ing %d " %(i+1))
            time.sleep(1)
    
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.ui=uic.loadUi("./thread_exe1.ui")
        #从ui中加载控件
        lineedit=self.ui.lineEdit
        bt1=self.ui.pushButton
        bt2=self.ui.pushButton_2
    
        #按钮连接槽
        bt1.clicked.connect(self.clck_1)
        bt2.clicked.connect(self.clck_2)
    
    def clck_1(self):
        for i in range(10):
            print("this is ui ing %d " %(i+1))
            time.sleep(1)
            
    def clck_2(self):
        self.my_thread=MyThread()
        self.my_thread.start()
        
     

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    # 展示窗口
    w.ui.show() # type: ignore

    app.exec()