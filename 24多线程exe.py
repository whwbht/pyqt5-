import json
import sys
import time

from PyQt5.QtCore import QThread,pyqtSignal
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5 import uic

class LoginThread(QThread):
    #创建自定义信号，字符串类型的使用很重要。dumps的使用，json等等
    start_login_signal=pyqtSignal(str)#这个地方是个技巧，与后面loads/get很方便，在操作字符串上。
    
    #子线程对象的创建,初始化
    def __init__(self):
        super().__init__()
        
    def login_by_requests(self,user_password_json):
        user_password_json=json.loads(user_password_json)
        print(user_password_json.get("user_name"))
        print(user_password_json.get("password"))          
    
    #子线程开始操作
    def run(self):
        while True:#让子线程一直运行，从而有能力接受UI线程的任务
            print("子线程ing")
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.ui=uic.loadUi("./FeiQQ.ui")
        #提取要操作的控件
        self.user_name_qwidget=self.ui.lineEdit
        self.password_qwidget=self.ui.lineEdit_2
        self.login_btn=self.ui.pushButton
        self.forget_btn=self.ui.pushButton_2
        self.text_browser=self.ui.textBrowser
        
        #确定按钮触发
        self.login_btn.clicked.connect(self.login)
        
        #创建子线程
        self.login_thread=LoginThread()
        # 创建的子线程进行绑定/信号触发就调用login_by_requests
        #子线程完成整个 消息的发送和接受/btn点击后，触发信号，信号触发槽，执行对应操作。信号和槽都是在子线程中进行定义。
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        #子线程开始工作
        self.login_thread.start()
        
        
    def login(self):
        #取出用户名和密码
        user_name=self.user_name_qwidget.text()
        password=self.password_qwidget.text()
        #发送信号，让子线程开始登陆
        self.login_thread.start_login_signal.emit(json.dumps({"user_name":user_name,"password":password}))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    # 展示窗口
    w.ui.show() # type: ignore

    app.exec()   