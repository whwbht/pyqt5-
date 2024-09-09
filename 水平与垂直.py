import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QGroupBox,QVBoxLayout,QHBoxLayout,QRadioButton

class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        container = QVBoxLayout()
        
        hobby_box=QGroupBox("hobby")
        v_layout=QVBoxLayout()
        btn1=QRadioButton("smoking")
        btn2=QRadioButton("drinking")
        btn3=QRadioButton("hair")
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        hobby_box.setLayout(v_layout)
        
        gender_box=QGroupBox("gender")
        h_layout=QHBoxLayout()
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        gender_box.setLayout(h_layout)
        
        container.addWidget(hobby_box)
        container.addWidget(gender_box)
        
        self.setLayout(container)


if __name__== '__main__':
    app=QApplication(sys.argv)
    
    w=MyWindow()
    w.show()
    
    app.exec()