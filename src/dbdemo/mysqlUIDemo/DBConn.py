from PyQt5 import QtGui
from PyQt5.QtSql import QSqlQuery, QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QApplication
import sys

class DBConn():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")  # 此处是mysql数据库
        self.db.setHostName("localhost")
        self.db.setUserName("winuser")
        self.db.setPassword("winuser")
        self.db.setDatabaseName("test")

    def __del__(self):
        self.db.close()
