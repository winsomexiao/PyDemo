import json
import logging
import time

import pandas
import sys
import tushare
from PyQt5.QtCore import pyqtSignal, QThread, QObject

import tushare as ts

logger = logging.getLogger('TushareWorkObject')
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

class TushareWorkObject(QObject):
    outSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        logging.debug("begin init")
        super(TushareWorkObject, self).__init__(parent)
        self.engine = create_engine('mysql://winuser:winuser@127.0.0.1/investdb?charset=utf8')
        with open("config.json", 'rt') as jsonFile:
            val = jsonFile.read()
            self.config = json.loads(val);

    def __del__(self):
        print("TushareWorkObject_del")

    def run(self):
        logging.debug("begin run")
        self.findLimitupStocks()
        self.outSignal.emit("finish")
        logging.debug(" run with trigger.emit")

    #
    def findLimitupStocks(self):
        logging.debug("begin findLimitupStocks")
        allData = tushare.get_today_all()
        upDate = time.strftime("%Y-%m-%d", time.localtime())
        upFileName = "UP" + upDate + ".csv"
        allDataFileName = "allData" + upDate + ".csv"
        outputAllDataFileDir = self.config['outputDir'] + "/" + allDataFileName
        outputUpDataFileDir = self.config['outputDir'] + "/" + upFileName
        upData = allData[allData.changepercent > 9.9]
        upData.to_csv(outputUpDataFileDir, encoding='gbk')
        logging.debug("allData.to_csv finish")
        allData.to_csv(outputAllDataFileDir, encoding='gbk')
        outputAllDataFileDir = self.config['outputDir'] + "/" + allDataFileName
        upData = pandas.read_csv(outputUpDataFileDir, encoding='gbk', index_col=0, dtype={'code': str})
        print(upData['code'])
        logging.debug("end findLimitupStocks")


    def getMoneySupply(self):
        logging.debug("begin getMoneySupply")
        moneySupply=tushare.get_money_supply()
        self.saveDb(moneySupply,"money_supply")
        logging.debug("end getMoneySupply")



    def saveDb(self,df,table):
        logging.debug("saveDB:"+table)
        #存入数据库
        try:
            df.to_sql(table,self.engine,if_exists='append')
        except:
            info=sys.exc_info()
            print(info[0],":",info[1])