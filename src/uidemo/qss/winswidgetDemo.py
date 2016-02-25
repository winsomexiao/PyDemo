import logging
import random

from PyQt5 import QtWidgets,QtCore

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QFrame, QLineEdit, QAbstractItemView, QGridLayout, QHBoxLayout, \
    QVBoxLayout, QMessageBox

__author__ = 'wins'

logger = logging.getLogger('winwidgetDemo')

class WinsWidget(QWidget):
    """主窗口。"""
    def __init__(self, parent=None):
        logger.info("_init__:begin")
        super(WinsWidget, self).__init__(parent)

        self.setObjectName('winsWidget')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle('wins的小工具')
        self.setWindowIcon(QIcon('icons/titleIcon.png'))

        self.resize(1000, 650)
        # 按钮start.
        self.btn_exit = QPushButton(self)
        self.btn_min = QPushButton(self)
        self.btn_max = QPushButton(self)
        self.btn_login = QPushButton("Unlogin", self)
        self.btn_search = QPushButton(self)
        self.btn_qry_stock = QPushButton(self)
        self.btn_add_stock = QPushButton(self)
        self.btn_del_stock = QPushButton(self)
        # 按钮end.

        # 标签start.
        self.lbe_pic = QLabel(self)
        self.header_hr = QLabel(self)
        self.header_icon = QLabel(self)
        self.header_text = QLabel(self)
        self.spacing = QLabel(self)
        self.spacing2 = QLabel(self)
        self.spacing3 = QFrame()
        self.spacing4 = QFrame()

        # -------
        # 输入框start.
        self.search_line = QLineEdit(self)
        # 输入框end.
        # -------
        # 列表框start.
        self.stockTableView = QtWidgets.QTableView(self)
        self.stockTableModel=QSqlTableModel(self)

        # -------
        # 布局与属性设置。
        self.mainLayout = QGridLayout()
        self.topLayout = QHBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.centerLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.rightLayout1 = QHBoxLayout()
        self.rightLayout2 = QVBoxLayout()
        self.rightLayout21 = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()
        self.bottomLayout1 = QVBoxLayout()
        self.playLayout = QHBoxLayout()
        self.set_buttons()
        self.set_labels()
        self.set_lines()
        self.load_stock_tableview()
        # -------
        # 其他功能。
        self.load_login()
        self.setLayout(self.set_layouts())
        logger.info("_init__:end")


 # 设置布局。
    def set_layouts(self):
        """
            布局。
        """
        # 头布局start.
        logger.info("set_layouts:begin")
        self.topLayout.setObjectName('Headerhbox')
        self.topLayout.addWidget(self.header_icon)
        self.topLayout.addWidget(self.header_text)
        self.topLayout.addWidget(self.spacing2)
        self.topLayout.addWidget(self.search_line)
        self.topLayout.addWidget(self.btn_search)
        self.topLayout.addStretch(1)
        self.topLayout.addWidget(self.lbe_pic)
        self.topLayout.addWidget(self.btn_login)
        self.topLayout.addWidget(self.spacing)
        self.topLayout.addWidget(self.btn_min)
        self.topLayout.addWidget(self.btn_max)
        self.topLayout.addWidget(self.btn_exit)
        self.topLayout.setSpacing(7)
        # -------
        self.mainLayout.addLayout(self.topLayout, 0, 0, Qt.AlignTop)
        self.mainLayout.addWidget(self.header_hr, 1, 0, Qt.AlignTop)
        # 头布局end.
        # --------
        # 中心布局start.
        #  左部分start.
        self.leftLayout.addWidget(self.btn_qry_stock)
        self.leftLayout.addWidget(self.btn_add_stock)
        self.leftLayout.addWidget(self.btn_del_stock)
        self.leftLayout.setSpacing(10)
        #  左部分end。
        # -------

        #  右部分end.
        # -------
        self.centerLayout.addLayout(self.leftLayout)
        self.centerLayout.addWidget(self.spacing3)
        self.centerLayout.addWidget(self.stockTableView)
        self.centerLayout.addLayout(self.rightLayout)
        self.centerLayout.setStretch(0, 180)
        self.centerLayout.setStretch(1, 1)
        self.centerLayout.setStretch(2, 0)
        self.centerLayout.setStretch(3, 830)
        self.centerLayout.setStretch(4, 0)
        self.mainLayout.addLayout(self.centerLayout, 2, 0, Qt.AlignTop | Qt.AlignLeft)
        # 中心布局end.
        # -------
        # 下部分start.
        self.mainLayout.addWidget(self.spacing4, 3, 0, Qt.AlignTop)
        self.mainLayout.addLayout(self.bottomLayout, 3, 0, Qt.AlignBottom)
        # self.mainLayout.addWidget(self.current_list, 2, 0, Qt.AlignBottom | Qt.AlignRight)
        # 下部分end.
        self.mainLayout.setRowStretch(1, 1)
        self.mainLayout.setRowStretch(2, 20)
        self.mainLayout.setRowStretch(3, 3)
        logger.info("set_layouts:end")
        return self.mainLayout


    def set_labels(self):
        """
            全部的标签组件。
        """
        p = QPixmap()
        p.load('icons/unlogin.png')
        p2 = QPixmap()
        p2.load('icons/titleIcon.png')
        # 头部装饰start。
        self.lbe_pic.setObjectName("headpic")
        self.lbe_pic.setPixmap(p.scaled(40, 40))
        self.header_hr.setObjectName('Headerhr')
        self.header_hr.setText("推荐")
        self.header_icon.setObjectName('HIcon')
        self.header_icon.setPixmap(p2.scaled(50, 50))
        self.header_text.setObjectName('HText')
        self.header_text.setText(" Music")


    def load_login(self):
        """
            登录
        """
        logger.info("load_login:")

    def quit_login(self):
        """
            退出
        """
        logger.info("quit_login:")

    def load_stock_tableview(self):
        """
            加载表格
        """
        logger.info("load_stock_tableview:begin")
        self.stockTableModel.setTable("t1")
        self.stockTableModel.select()
        self.stockTableModel.setEditStrategy(QSqlTableModel.OnManualSubmit)
        # 数据更新的策略，详细可以查看Qt文档
        self.stockTableView.setModel(self.stockTableModel)
        self.stockTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stockTableView.setSelectionMode(QAbstractItemView.ExtendedSelection)

        #self.stockTableView.setGeometry(QtCore.QRect(290, 110, 471, 221))
        self.stockTableView.setObjectName("stockTableView")

        logger.info("load_stock_tableview:end")

    def set_buttons(self):
        """
            全部的按钮组件。
        """
        # 退出。
        logger.info("set_buttons:begin")
        self.btn_exit.setObjectName('exit')
        self.btn_exit.setText('×')
        self.btn_exit.clicked.connect(self.close)
        self.btn_exit.setToolTip('退出')
        # 最小化。
        self.btn_min.setObjectName('mini')
        self.btn_min.setText('-')
        self.btn_min.clicked.connect(self.showMinimized)
        self.btn_min.setToolTip('最小化')
        # 最大化。
        self.btn_max.setObjectName('maxi')
        self.btn_max.setText('□')
        self.btn_max.setToolTip('^_^此功能已上火星')
        # 登陆。
        self.btn_login.setObjectName('login')
        self.btn_login.setToolTip('登陆')
        # 搜索。
        self.btn_search.setObjectName('searchBtn')
        self.btn_search.resize(48, 48)

        # 查询。
        self.btn_qry_stock.setObjectName('btnQryStock')
        self.btn_qry_stock.setIcon(QIcon('icons/qryBtn.png'))
        self.btn_qry_stock.setText("查询")
        self.btn_qry_stock.clicked.connect(self.qryStockFunc)
        # 增加。
        self.btn_add_stock.setObjectName('btnAddStock')
        self.btn_add_stock.setIcon(QIcon('icons/addBtn.png'))
        self.btn_add_stock.setText("增加")
        self.btn_add_stock.clicked.connect(self.addStockFunc)
        # 删除。
        self.btn_del_stock.setObjectName('btnDelStock')
        self.btn_del_stock.setIcon(QIcon('icons/delBtn.png'))
        self.btn_del_stock.setText("删除")
        self.btn_del_stock.clicked.connect(self.delStockFunc)
        logger.info("set_buttons:end")


    def set_lines(self):
        """
            输入框。
        """
        logger.info("set_lines:begin")
        self.search_line.setObjectName('SearchLine')
        self.search_line.setPlaceholderText('搜索')
        logger.info("set_lines:end")

    def set_sliders(self):
        """
            滚动组件。
        """
        logger.info("set_sliders:begin")
        self.slider.setObjectName("slider")
        self.slider.setOrientation(Qt.Horizontal)
        logger.info("set_sliders:end")


    def hide_index(self):
        """
            隐藏主页, 显示歌单详细信息。
        """
        logger.info("hide_index")

    def show_index(self):
        """
            显示主页。
        """
        logger.info("show_index")
    # 切换页面end.



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

    """按键绑定。。"""
    def keyPressEvent(self, event):
        logger.info("keyPressEvent:")
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Enter-1:
            self.song_search()

    """退出窗口时做的一些事。"""
    def closeEvent(self, event):
        # 退出时保存歌曲列表缓存。
        logger.info("showEvent:")


    """界面开始前的一些事。"""
    def showEvent(self, event):
       logger.info("showEvent:")



#查询按钮关联的槽函数
    def qryStockFunc(self):
        #self.db.execSQL("select * from t1")
        logger.info("qryStockFunc:")

#插入按钮关联的槽函数
    def addStockFunc(self):
        logger.info("addStockFunc:begin")
        f1=random.randint(1, 99)
        self.myTableModel.insertRows(0, 1)
        self.myTableModel.setData(self.myTableModel.index(0, 0), f1)
        self.myTableModel.setData(self.myTableModel.index(0, 1), "test")
        self.myTableModel.submitAll()
        logger.info("addStockFunc:end")

    def delStockFunc(self):
        logger.info("delStockFunc:begin")
        rs=list(map(lambda x:x.row(),self.myTableView.selectedIndexes()))
        if len(rs)==0:
            QMessageBox.information(self,'提醒','请先选中至少一行，再点击此按钮！')
            return
            for i in reversed(rs):
                self.myTableModel.removeRows(i,1)
                self.myTableModel.submitAll()
        logger.info("delStockFunc:end")