#coding=utf-8
import xlrd
import os
import xlwt

def DriverDir(dirPath):
    filePathlist = [];
    for parent,filenames in os.walk(dirPath):
        for filename in filenames:
            if((filenames.find('.xls') != -1) and (filenames.find('.xlsx') != -1)):
                filename = parent + '\\' + filename
                filePathlist.append(filename)
    '''遍历处所有文件'''
    return filePathlist

class omsExcel:
    def readDirData(self, dirPath):
        '''遍历文件夹下所有xls,xlsm文件  读取数据'''
        fileList = DriverDir(dirPath)
        dataList = []
        for filePath in fileList:
            singleDataList = self.readFileData(filePath)
            dataList.append(singleDataList)
        '''datalist[0][0][0]'''
        return dataList

    def readFileData(self, filePath):
        '''读取单独文件数据'''
        listData = []
        wkBook = xlrd.open_workbook(filePath)
        for wkSht in wkBook.sheets():
            nrows = wkSht.nrows
            ncols = wkSht.ncols
            '''第一行标题数据不读取'''
            for rownum in range(1, nrows):
                row = wkSht.row_values(rownum)
                if row:
                    rowData = {}
                    for col in range(0, ncols):
                        rowData[col] = row[col]

                    listData.append(rowData)
        return listData


    def writeFileData(self, filePath, dataList):
        '''写入文件数据'''
        writeBk = xlwt.Workbook()
        writeSht = writeBk.add_sheet("导出结果")
        '''三层数据，最外层为workbook 第二层行，第三次为列'''
        for wb  in range(0, len(dataList)):
            for row in range(0, len(dataList[0])):
                for col in range(0, len(dataList[0][0])):
                    writeSht.write(row, col, dataList[wb][row][col])
        writeBk.save(filePath)


#coding=utf-8
import sqlite3

class dbOperator:

    def __init__(self):
        print("DBoperator")

    def ConnectDb(self):
        try:
            print("connect")
            self.conn = sqlite3.connect("omsDB.db")
        except Exception as ex:
            print(ex)
        else:
            print("create")
            self.createTable()

    '''创建'''
    def createTable(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS t_oms_data
                        ( orderID         text           primary key not null,
                          accountName     text            ,
                          zhifubaoName    text            ,
                          payableMoney    text            ,
                          postMoney       text            ,
                          zhufuPoint      text            ,
                          totalMoney      text            ,
                          backPoint       text            ,
                          realMoney       text            ,
                          realzhifuPoint  text            ,
                          orderState      text            ,
                          customMsg       text            ,
                          customName      text            ,
                          recvAddress     text            ,
                          postWay         text            ,
                          phoneNum        text            ,
                          telphoneNum     text            ,
                          odCreateTime    text            ,
                          odpayTime       text            ,
                          goodsTitle      text            ,
                          goodsType       text            ,
                          logisticsNum    text            ,
                          logisticsCmy    text            ,
                          odRemark        text            ,
                          goodsTotal      text            ,
                          storeID         text            ,
                          storeName       text            ,
                          odCloseReason   text            ,
                          serverMoney     text            ,
                          customSerMoney  text            ,
                          invoiceName     text            ,
                          isTelphonOD     text            ,
                          odPartInfo      text            ,
                          earnestRank     text            ,
                          modifySku       text            ,
                          modifyAdd       text            ,
                          exceptInfo      text            ,
                          tianmaoCard     text            ,
                          jifenbaoCart    text            ,
                          isO2O           text            );''')

    def putValue(self, datalist, singleFile = True):
        sqlStr = ''
        realList = []
        if singleFile == True:
            realList.append(datalist)
        else:
            realList = datalist
        print(realList)
        for wb in range(0, len(realList)):
            for row in range(0, len(realList[0])):
                sqlStr = "INSERT INTO t_oms_data VALUES("
                for col in range(0, len(realList[0][0])):
                    newStr = str(realList[wb][row][col])
                    if(newStr.find("'") != -1):
                        newStr = newStr.replace("'","")
                    tmpStr = "'%s'" % (newStr)
                    if col != len(realList[0][0]) - 1:
                        tmpStr += ","
                    sqlStr += tmpStr
                sqlStr += ");"
                '''插入一行数据'''
                try:
                    print(sqlStr)
                    cur = self.conn.cursor()
                    cur.execute(sqlStr)
                except Exception as ex:
                    print(ex)
                    continue
                else:
                    self.conn.commit()

    def getFindValue(self, sqlStr):
        #sqlStr = "select * from t_oms_data where accountName = '%s'" %(accountName)
        cur = self.conn.cursor()
        cur.execute(sqlStr)
        rows = cur.fetchall()
        cur.close()
        '''查询结果是二维'''
        return rows

    def closeDb(self):
        if(self.conn == None):
            self.conn.close()





if __name__=="__main__":

    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    cur.execute("select * from t1")
    res = cur.fetchall()
    print(res[0][0])