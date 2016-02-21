# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowIcon(QtGui.QIcon('./gita.ico'))
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        openAction = self.menu.addAction('open')
        saveAction = self.menu.addAction('save')
        saveAsAction = self.menu.addAction('save as')
        openAction.setShortcut('Ctrl+O')
        saveAction.setShortcut('Ctrl+S')
        self.connect(openAction, QtCore.SIGNAL("triggered()"), self.openFile)
        self.connect(saveAction, QtCore.SIGNAL("triggered()"), self.saveFile)
        self.file = None
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "记事本", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))

    def openFile(self):
        self.file = QtGui.QFileDialog.getOpenFileName(self)
        if self.file:
            self.textEdit.setText(open(self.file).read())
            MainWindow.setWindowTitle(_translate("MainWindow", self.file, None))

    def saveFile(self):
        plainText = self.textEdit.toPlainText()
        if not self.file:
            self.file = QtGui.QFileDialog.getSaveFileName(self)
        MainWindow.setWindowTitle(_translate("MainWindow", self.file, None))
        with open(self.file, 'w') as f:
            f.write(plainText)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())