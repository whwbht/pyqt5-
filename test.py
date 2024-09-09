import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QLabel,QLineEdit,QDesktopWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)#参数传递。对象需要传参。python

    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")
    w.setWindowIcon
    
    # btn=QPushButton("按钮")
    # btn.setParent(w)
    w.resize(1000,800)
    # w.move(0,0)
    windowCenter=QDesktopWidget().availableGeometry().center()
    # print(windowCenter)
    x=windowCenter.x()
    y=windowCenter.y()
    
    
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x-width/2,y-height/2)
    
    # label = QLabel("账号",w)
    # label.setGeometry(10,20,30,20)
    
    
    # edit=QLineEdit(w)
    # edit.setPlaceholderText("print your edit")
    # edit.setGeometry(55,20,200,20)
    
    # btn = QPushButton("注册", w)
    # btn.setGeometry(50, 80, 70, 30)
    
    

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()