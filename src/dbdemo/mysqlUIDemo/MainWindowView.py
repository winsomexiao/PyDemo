import random
import sys
import time

from PyQt5 import QtCore
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView, QAbstractItemView
from PyQt5.QtWidgets import QMainWindow

from src.dbdemo.mysqlUIDemo.DBConn import DBConn
from src.dbdemo.mysqlUIDemo.UI_Test import Ui_myMainWindow


class MyMainWindowView(QMainWindow, Ui_myMainWindow):
    # 增加自定义信号
    _selfSignal = QtCore.pyqtSignal(str)


    def __init__(self):
        super(MyMainWindowView, self).__init__()
        self.setupUi(self)
        self._selfSignal.connect(self.allBtnShow)
        self.actionAbout.triggered.connect(self.aboutFun)
        self.actionExit.triggered.connect(QApplication.instance().quit)
        self.actionChange_title.triggered.connect(self.changeTitle)

        self.qryBtn.clicked.connect(self.qryFunc)
        self.addBtn.clicked.connect(self.addFunc)
        self.delBtn.clicked.connect(self.delFunc)
        self.del2Btn.clicked.connect(self.del2Func)
        self.db=DBConn()
        #model 与 view绑定
        self.myTableModel=QSqlTableModel(self)
        self.myTableModel.setTable("t1")
        self.myTableModel.select()
        self.myTableModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        # 数据更新的策略，详细可以查看Qt文档
        self.myTableView.setModel(self.myTableModel)
        self.myTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.myTableView.setSelectionMode(QAbstractItemView.ExtendedSelection)

# 增加自定义槽函数
    def allBtnHide(self):
        print("test2")
        self.pushButton.hide()
        self.pushButton_2.hide()
        time.sleep(1)
        self._selfSignal.emit("我是自定义信号")
        # self.pushButton_3.hide()


#增加自定义槽函数
    def allBtnShow(self, signalstr):
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.setText(signalstr)

# 增加自定义槽函数
    def aboutFun(self):
           QMessageBox.about( self, 'PyQt', "About")

    def changeTitle(self):
          self.setWindowTitle("xxx Window")

#查询按钮关联的槽函数
    def qryFunc(self):
        #self.db.execSQL("select * from t1")
        QMessageBox.about( self, 'qryFuncCall', "qryFunc")

#插入按钮关联的槽函数
    def addFunc(self):
        # f1=random.randint(1, 9999)
        # sql  = "insert into t1(f1,f2) values (%s,%s)"%(f1,f1)
        # self.db.execSQL(sql)
        f1=random.randint(1, 99)
        self.myTableModel.insertRows(0, 1)
        self.myTableModel.setData(self.myTableModel.index(0, 0), f1)
        self.myTableModel.setData(self.myTableModel.index(0, 1), "test")
        self.myTableModel.submitAll()
        QMessageBox.about( self, 'addFuncCall', "addFunc")

    # #删除按钮关联的槽函数
    def del2Func(self):
         if self.myTableModel.select() :
            if self.myTableModel.rowCount() != 0:
                for i in self.myTableView.selectedIndexes():
                    self.myTableModel.removeRows(i.row(), 1)
                self.myTableModel.submitAll()

# #删除按钮关联的槽函数
#     def delFunc(self):
#         if self.myTableModel.select() :
#            if self.myTableModel.rowCount() != 0:
#                index = self.myTableView.currentIndex()
#                self.myTableModel.removeRows(0,1)
#                self.myTableModel.submitAll()
#         QMessageBox.about( self, 'delFuncCall', "delFunc")



    def delFunc(self):
             rs=list(map(lambda x:x.row(),self.myTableView.selectedIndexes()))
             if len(rs)==0:
                 QMessageBox.information(self,'提醒','请先选中至少一行，再点击此按钮！')
                 return
             for i in reversed(rs):
                 self.myTableModel.removeRows(i,1)
             self.myTableModel.submitAll()


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 载入qt应用程序架构，所有qt通用
    myshow = MyMainWindowView()
    myshow.show()
    sys.exit(app.exec_())
