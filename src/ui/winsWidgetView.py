#coding=utf-8
import logging
import random

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtSql import QSqlTableModel, QSqlDatabase
from PyQt5.QtWidgets import QWidget, QMessageBox, QAbstractItemView
from PyQt5.QtCore import Qt, QSize
from src.ui.winsWidget import Ui_Wins_Widget

__author__ = 'wins'

logger = logging.getLogger('winwidgetDemo')

class WinsWidgetView(QWidget, Ui_Wins_Widget):

        def __init__(self,parent=None):
            logger.debug("_init__:begin")
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

            logger.debug("_init__:end")



        """重写鼠标事件，实现窗口拖动。"""
        def mousePressEvent(self, event):
            logger.debug("mousePressEvent:")
            if event.buttons() == Qt.LeftButton:
                self.m_drag = True
                self.m_DragPosition = event.globalPos()-self.pos()
                event.accept()

        def mouseMoveEvent(self, event):
            logger.debug("mouseMoveEvent:")
            try:
                if event.buttons() and Qt.LeftButton:
                    self.move(event.globalPos()-self.m_DragPosition)
                    event.accept()
            except AttributeError:
                pass

        def mouseReleaseEvent(self, event):
            logger.debug("mouseReleaseEvent:")
            self.m_drag = False


 # 设置布局。
        def set_layouts(self):
            logger.debug("set_layouts:begin")
            self.page1group.setAlignment(Qt.AlignCenter)
            self.page1layout.setAlignment(Qt.AlignCenter)
            logger.debug("set_layouts:end")

# 设置按钮
        def set_buttons(self):
            logger.debug("set_buttons:begin")
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
            self.qryBtn.setAutoRaise(True)
            self.qryBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            # 增加。
            self.addBtn.setIcon(QIcon('icons/addBtn.png'))
            self.addBtn.setText("增加")
            self.addBtn.clicked.connect(self.addFunc)
            self.addBtn.setAutoRaise(True)
            self.addBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            # 删除。
            self.delBtn.setIcon(QIcon('icons/delBtn.png'))
            self.delBtn.setText("删除")
            self.delBtn.clicked.connect(self.delFunc)
            self.delBtn.setAutoRaise(True)
            self.delBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            logger.debug("set_buttons:end")

            self.toolBox.setCurrentIndex(0)
            self.toolBox.setItemIcon(0,QIcon("icons/homeIcon.png"))
            self.toolBox.setItemIcon(1,QIcon("icons/homeIcon.png"))

            self.page1btn1.setIcon(QIcon("icons/homeIcon.png"))
            self.page1btn1.setText(self.tr("首页"))
            self.page1btn1.setIconSize(QSize(40,40))
            self.page1btn1.setAutoRaise(True)
            self.page1btn1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page1btn2.setIcon(QIcon("icons/graphIcon.png"))
            self.page1btn2.setText(self.tr("图表"))
            self.page1btn2.setIconSize(QSize(40,40))
            self.page1btn2.setAutoRaise(True)
            self.page1btn2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page1btn3.setIcon(QIcon("icons/taskIcon.png"))
            self.page1btn3.setText(self.tr("任务"))
            self.page1btn3.setIconSize(QSize(40,40))
            self.page1btn3.setAutoRaise(True)
            self.page1btn3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page1btn4.setIcon(QIcon("icons/clockIcon.png"))
            self.page1btn4.setText(self.tr("提醒"))
            self.page1btn4.setIconSize(QSize(40,40))
            self.page1btn4.setAutoRaise(True)
            self.page1btn4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page1btn5.setIcon(QIcon("icons/favIcon.png"))
            self.page1btn5.setText(self.tr("收藏"))
            self.page1btn5.setIconSize(QSize(40,40))
            self.page1btn5.setAutoRaise(True)
            self.page1btn5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page1btn6.setIcon(QIcon("icons/kxianIcon.png"))
            self.page1btn6.setText(self.tr("k线"))
            self.page1btn6.setIconSize(QSize(40,40))
            self.page1btn6.setAutoRaise(True)
            self.page1btn6.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


            self.page2btn1.setIcon(QIcon("icons/marketIcon.png"))
            self.page2btn1.setText(self.tr("行情"))
            self.page2btn1.setIconSize(QSize(40,40))
            self.page2btn1.setAutoRaise(True)
            self.page2btn1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page2btn2.setIcon(QIcon("icons/stockIcon.png"))
            self.page2btn2.setText(self.tr("证券"))
            self.page2btn2.setIconSize(QSize(40,40))
            self.page2btn2.setAutoRaise(True)
            self.page2btn2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page2btn3.setIcon(QIcon("icons/contactIcon.png"))
            self.page2btn3.setText(self.tr("收益率"))
            self.page2btn3.setIconSize(QSize(40,40))
            self.page2btn3.setAutoRaise(True)
            self.page2btn3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

            self.page2btn4.setIcon(QIcon("icons/calIcon.png"))
            self.page2btn4.setText(self.tr("绩效"))
            self.page2btn4.setIconSize(QSize(40,40))
            self.page2btn4.setAutoRaise(True)
            self.page2btn4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


        def set_labels(self):
            logger.debug("set_labels:begin")
            titlePix = QPixmap()
            titlePix.load('icons/titleIcon.png')
            self.headIcon.setPixmap(titlePix.scaled(40, 40))
            self.headTitle.setText("Wins百宝箱")
            self.topSpace.setText("")
            logger.debug("set_labels:end")

        def set_lines(self):
            logger.debug("set_lines:begin")
            self.searchInput.setPlaceholderText('搜索')
            logger.debug("set_lines:end")

        def load_tableview(self):
            logger.debug("load_tableview:begin")

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

            logger.debug("load_tableview:end")

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
