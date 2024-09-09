import sys
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QWidget,QPushButton,QGroupBox,QMainWindow,QLineEdit,QGridLayout
from PyQt5.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("计算器")
        # 准备数据
        data = {
            0: ["7", "8", "9", "+", "("],
            1: ["4", "5", "6", "-", ")"],
            2: ["1", "2", "3", "*", "<-"],
            3: ["0", ".", "=", "/", "C"]
        }
        
        #整体垂直布局
        layout=QVBoxLayout() 
        
        # 输入框
        edit=QLineEdit()
        edit.setPlaceholderText("please enter your as")
        layout.addWidget(edit)    
       
        # 网格布局
        grid = QGridLayout()
        for line_number, line_data in data.items():
            # 此时line_number是第几行，line_data是当前行的数据
            for col_number, number in enumerate(line_data):
                # 此时col_number是第几列，number是要显示的符号
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)
        
        layout.addLayout(grid)
        
        self.setLayout(layout)
        

if __name__== '__main__':
    app=QApplication(sys.argv)
    
    w=MyWindow()
    w.show()
    
    app.exec()