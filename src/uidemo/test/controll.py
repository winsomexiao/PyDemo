import logging

from PyQt5.QtCore import QTimer

from src.uidemo.test.DemoThreadView import demoMainWindowView
from src.uidemo.test.workThread import WorkThread


class demoController:
    def __init__(self):
        logging.debug("begin __init__")
        self.timer=QTimer()
        self.timer.timeout.connect(demoMainWindowView.countTime)

    def work(self):

        self.timer.start(1000)               #计时器每秒计数
        workThread=WorkThread()
        workThread.start()              #计时开始
        workThread.trigger.connect(demoMainWindowView.timeStop)   #当获得循环完毕的信号时，停止计数

