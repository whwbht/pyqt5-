import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QWidget,QPushButton,QGroupBox,QMainWindow
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.resize(300,300)
        self.setWindowTitle("vertical layout")
        
        layout=QVBoxLayout()
        
        btn1=QPushButton("button1")
        layout.addWidget(btn1)
        
        btn2=QPushButton("button2")
        layout.addWidget(btn2)
        
        btn3=QPushButton("button3")
        layout.addWidget(btn3)
        
        # layout.addStretch(2)
        
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget子类
    w = MyWindow()
    w.show()

    app.exec()
    