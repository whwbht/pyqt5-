import  sys

from PyQt5.QtWidgets import QWidget, QLabel , QApplication

class mywnd(QWidget):

    def __init__(self):
        super(mywnd, self).__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("这是文字~~" )
        label.setStyleSheet("font-size:30px;color:red")
        label.setParent(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = mywnd()

    #设置窗口标题
    w.setWindowTitle("qwidget")

    # 展示窗口
    w.show()

    # 程序进行循环等待状态
    app.exec()