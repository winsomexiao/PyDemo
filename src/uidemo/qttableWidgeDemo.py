#coding=utf-8
#soruce http://blog.csdn.net/vah101/article/details/6215066
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import *



class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.MyTable = QTableWidget(4,3)
        # #设置为不允许编辑的，默认是可以比编辑的。
        # self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # #设置整行选中，默认是选中单元格
        # self.MyTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        # #设置为不能选择
        # self.MyTable.setSelectionMode(QAbstractItemView.NoSelection)
        # #设置表头的显示和隐藏（水平和垂直）
        # self.MyTable.verticalHeader().setVisible(False)
        # self.MyTable.horizontalHeader().setVisible(False)
        self.MyTable.setHorizontalHeaderLabels(['姓名','身高','体重'])
        newItem = QTableWidgetItem("松鼠")
        self.MyTable.setItem(0, 0, newItem)
        newItem = QTableWidgetItem("10cm")
        self.MyTable.setItem(0, 1, newItem)
        newItem = QTableWidgetItem("60g")
        self.MyTable.setItem(0, 2, newItem)
        newItem = QTableWidgetItem("袋鼠")
        self.MyTable.setItem(2, 0, newItem)
        newItem = QTableWidgetItem("150cm")
        self.MyTable.setItem(2, 1, newItem)
        newItem = QTableWidgetItem("60Kg")
        self.MyTable.setItem(2, 2, newItem)
        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)
    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWindow = MyDialog()
    myWindow.show()
    sys.exit(app.exec_())