from PyQt5 import QtGui
from PyQt5.QtSql import QSqlQuery, QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QApplication
import sys

class DBManager():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("localhost")
        self.db.setUserName("winuser")
        self.db.setPassword("winuser")
        self.db.setDatabaseName("test")

    def __del__(self):
        self.db.close()

    def execSQL(self,sql):
        self.db.open()
        self.query = QSqlQuery()
        self.query.exec_(sql)
        self.query.exec_("commit")

    def close(self):
        self.db.close()

class Model(QSqlTableModel):
    def __init__(self, parent):
        QSqlTableModel.__init__(self, parent)
        self.setTable("t1")
        # 这一步应该是执行查询的操作，不太理解
        self.select()
        # 数据更新的策略，详细可以查看Qt文档
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)


class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        vbox = QVBoxLayout(self)
        self.view = QTableView()
        self.model = Model(self.view)
        self.view.setModel(self.model)
        vbox.addWidget(self.view)


if __name__ == "__main__":
    a = QApplication(sys.argv)
    db=DBManager()
    db.execSQL("delete from t1")
    db.execSQL("create table if not exists t1 (f1 integer primary key,f2 varchar(20))")
    db.execSQL(u"insert into t1 values(1,'我1')")
    db.execSQL(u"insert into t1 values(2,'我test4')")
    db.close()
    w = TestWidget()
    w.show()
    sys.exit(a.exec_())
