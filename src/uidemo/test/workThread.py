from PyQt5.QtCore import QThread, pyqtSignal


class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread,self).__init__()

    def run(self):
        for i in range(203300030):
            pass
        self.trigger.emit()         #循环完毕后发出信号
