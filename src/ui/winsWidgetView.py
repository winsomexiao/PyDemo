#coding=utf-8
import logging
import random

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QWidget, QMessageBox, QAbstractItemView
from PyQt5.QtCore import Qt
from src.ui.winsWidget import Ui_Wins_Widget

__author__ = 'wins'

logger = logging.getLogger('winwidgetDemo')

class WinsWidgetView(QWidget, Ui_Wins_Widget):

        def __init__(self,parent=None):
            logger.info("_init__:begin")
            super(WinsWidgetView, self).__init__(parent)
            self.setupUi(self)
            self.dbPath="test.db"
            self.curTable="test2"

            self.setObjectName('winsWidget')
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setWindowTitle('wins的小工具')
            self.setWindowIcon(QIcon('icons/titleIcon.png'))

            self.tableModel=QSqlTableModel(self,QSqlDatabase.addDatabase('QSQLITE'))

            self.set_buttons()
            self.set_labels()
            self.set_lines()
            self.load_tableview()

            logger.info("_init__:end")



        """重写鼠标事件，实现窗口拖动。"""
        def mousePressEvent(self, event):
            logger.info("mousePressEvent:")
            if event.buttons() == Qt.LeftButton:
                self.m_drag = True
                self.m_DragPosition = event.globalPos()-self.pos()
                event.accept()

        def mouseMoveEvent(self, event):
            logger.info("mouseMoveEvent:")
            try:
                if event.buttons() and Qt.LeftButton:
                    self.move(event.globalPos()-self.m_DragPosition)
                    event.accept()
            except AttributeError:
                pass

        def mouseReleaseEvent(self, event):
            logger.info("mouseReleaseEvent:")
            self.m_drag = False


 # 设置布局。
        def set_layouts(self):
            logger.info("set_layouts:begin")
            logger.info("set_layouts:end")

# 设置按钮
        def set_buttons(self):
            logger.info("set_buttons:begin")
            self.closeBtn.setText('×')
            self.closeBtn.clicked.connect(self.close)
            self.closeBtn.setToolTip('退出')
            # 最小化。
            self.minBtn.setText('-')
            self.minBtn.clicked.connect(self.showMinimized)
            self.minBtn.setToolTip('最小化')
            # 最大化。
            self.maxBtn.setText('□')
            self.maxBtn.setToolTip('^_^此功能已上火星')
            # 登陆。
            self.loginBtn.setText('')
            self.loginBtn.setToolTip('登陆')
            # 搜索输入框。
            self.searchInput.resize(48, 48)
            # 搜索按钮
            self.searchBtn.setText('')
            self.searchBtn.setToolTip('点击搜索')

            # 查询。
            self.qryBtn.setIcon(QIcon('icons/qryBtn.png'))
            self.qryBtn.setText("查询")
            self.qryBtn.clicked.connect(self.qryFunc)
            # 增加。
            self.addBtn.setIcon(QIcon('icons/addBtn.png'))
            self.addBtn.setText("增加")
            self.addBtn.clicked.connect(self.addFunc)
            # 删除。
            self.delBtn.setIcon(QIcon('icons/delBtn.png'))
            self.delBtn.setText("删除")
            self.delBtn.clicked.connect(self.delFunc)
            logger.info("set_buttons:end")


        def set_labels(self):
            logger.info("set_labels:begin")
            titlePix = QPixmap()
            titlePix.load('icons/titleIcon.png')
            self.headIcon.setPixmap(titlePix.scaled(40, 40))
            self.headTitle.setText("Wins百宝箱")
            self.topSpace.setText("")
            logger.info("set_labels:end")

        def set_lines(self):
            logger.info("set_lines:begin")
            self.searchInput.setPlaceholderText('搜索')
            logger.info("set_lines:end")

        def load_tableview(self):
            logger.info("load_tableview:begin")

             ###self.model数据初始化
            self.tableModel.database().setDatabaseName(self.dbPath)
            self.tableModel.database().open()
            self.tableModel.setTable(self.curTable)
            self.tableModel.select()

            self.tableModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
            # 数据更新的策略，详细可以查看Qt文档
            self.tableView.setModel(self.tableModel)
            self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)

            logger.info("load_tableview:end")

    #查询按钮关联的槽函数
        def qryFunc(self):
            #self.db.execSQL("select * from t1")
            QMessageBox.about( self, 'qryFuncCall', "qryFunc")

    #插入按钮关联的槽函数
        def addFunc(self):
            f1=random.randint(1, 99)
            self.tableModel.insertRows(0, 1)
            self.tableModel.setData(self.tableModel.index(0, 0), f1)
            self.tableModel.setData(self.tableModel.index(0, 1), "test")
            self.tableModel.submitAll()
            QMessageBox.about( self, 'addFuncCall', "addFunc")


        def delFunc(self):
                 rs=list(map(lambda x:x.row(),self.tableView.selectedIndexes()))
                 if len(rs)==0:
                     QMessageBox.information(self,'提醒','请先选中至少一行，再点击此按钮！')
                     return
                 for i in reversed(rs):
                     self.tableModel.removeRows(i,1)
                 self.tableModel.submitAll()
