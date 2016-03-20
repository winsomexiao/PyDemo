import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber, QPushButton, QMainWindow

from src.uidemo.test.controll import demoController


class demoMainWindowView(QMainWindow):
    def __init__(self):
        super(demoMainWindowView, self).__init__()
        self.top=QWidget()
        self.layout=QVBoxLayout(self.top)
        self.lcdNumber=QLCDNumber()
        self.layout.addWidget(self.lcdNumber)
        self.button=QPushButton("测试")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(demoController.work)

    def countTime(self):
        global  sec
        sec+=1
        demoMainWindowView.lcdNumber.display(sec)          #LED显示数字+1

    def timeStop(self):
        self.timer.stop()
        print("运行结束用时", demoMainWindowView.lcdNumber.value())
        global sec
        sec=0


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 载入qt应用程序架构，所有qt通用
    myshow = demoMainWindowView()
    myshow.show()
    sys.exit(app.exec_())