#coding=utf-8
import random
import sys

import sqlite3

from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from src.dbdemo.sqliteUIDemo.mainWindowUI import Ui_MainWindow


class MainWindowView(QMainWindow, Ui_MainWindow):
        def __init__(self,dbPath,tblName,parent=None):
            super(MainWindowView, self).__init__(parent)
            self.setupUi(self)

            self.addBtn.clicked.connect(self.addBtnFunc)
            self.updBtn.clicked.connect(self.updBtnFunc)
            self.delBtn.clicked.connect(self.delBtnFunc)

            self.dbPath="test.db"
            self.curTable="test2"

            ###tableView与model绑定
            self.tableModel=QSqlTableModel(self,QSqlDatabase.addDatabase('QSQLITE'))
            self.tableModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
            self.tableView.setModel(self.tableModel)

            ###self.model数据初始化
            self.tableModel.database().setDatabaseName(self.dbPath)
            self.tableModel.database().open()
            self.tableModel.setTable(self.curTable)
            self.tableModel.select()

        #新增按钮关联的槽函数
        def addBtnFunc(self,event):
            f1=random.randint(1, 99)
            self.tableModel.insertRows(0, 1)
            self.tableModel.setData(self.tableModel.index(0, 0), f1)
            self.tableModel.setData(self.tableModel.index(0, 1), "test")
            self.tableModel.submitAll()

        #修改按钮关联的槽函数
        def updBtnFunc(self,event):
             QMessageBox.information( self, '提醒', "updBtnFunc Call!")


        #删除按钮关联的槽函数
        def delBtnFunc(self,event):
             rs=list(map(lambda x:x.row(),self.tableView.selectedIndexes()))
             if len(rs)==0:
                 QMessageBox.information(self,'提醒','请先选中至少一行，再点击此按钮！')
                 return
             for i in reversed(rs):
                 self.tableModel.removeRows(i,1)
             self.tableModel.submitAll()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindowView('test.db','test2')
    view.show()
    sys.exit(app.exec_())
