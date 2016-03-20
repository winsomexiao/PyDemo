import json
import logging
import time

import pandas
import tushare as ts
from PyQt5.QtCore import pyqtSignal, QThread

logger = logging.getLogger('LimitupStockThread')

class DatayesThread(QThread):
    _selfSignal = pyqtSignal()

    def __init__(self,parent=None):
        logging.debug("begin init")
        super(DatayesThread,self).__init__(parent)
        ts.set_token('edc37d879a4757aae38b00cf49cc2dffe936bf3efb0f700c3cbb1f798ec82d5d')


    def __del__(self):
        logging.debug("begin del")
        self.wait()
        logging.debug("end del")


    def run(self):
        logging.debug("begin run")

        logging.debug("begin findDatayes_data")

        print(ts.get_token())
        mkt = ts.Market()
        df = mkt.TickRTSnapshot(securityID='000001.XSHE')
        print("df:"+df)
        logging.debug("end findDatayes_data")

        #self.findDatayes_data()

        self._selfSignal.emit()
        logging.debug(" run with trigger.emit")
    #
    def findDatayes_data(self):
         logging.debug("begin findDatayes_data")

         print(ts.get_token())
         mkt = ts.Market()
         df = mkt.TickRTSnapshot(securityID='000001.XSHE')
         print("df:"+df)
         logging.debug("end findDatayes_data")

