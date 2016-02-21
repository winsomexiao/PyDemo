# -*- coding: utf-8 -*-
import os
import platform
import sqlite3
import sys


from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, \
    QLineEdit, QTableView, QFileDialog, QMessageBox, QDialog, QListWidget, QGroupBox, QComboBox, QInputDialog, \
    QGridLayout



class SqliteDbTableEditer(QWidget):
    #Db=sqlite3.connect("test.db")
    def __init__(self,dbPath,tblName='',parent=None):

        self.app=QApplication(sys.argv)
        self.SqliteDbTypes=['integer','real','text','blob']
        self.DbPath,self.CurrentTable=dbPath,tblName
        #连接数据库
        self.Db=sqlite3.connect(self.DbPath)
        #构建Gui组件
        super(SqliteDbTableEditer,self).__init__(parent)
        self.setWindowTitle('Sqlite数据库表修改器')
        screen=QDesktopWidget().availableGeometry(0)
        self.setGeometry(screen.width()/3/2-1,
                         screen.height()/5/2-1,
                         screen.width()*2/3,
                         screen.height()*4/5
                         )
        #lay
        lay=QVBoxLayout()
        self.setLayout(lay)
        #数据库表设置控件
        ##layDb
        layDb=QHBoxLayout()
        lay.addLayout(layDb)
        ###lblDb
        lblDb=QLabel('数据库：')
        layDb.addWidget(lblDb)
        ###self.leDb
        self.leDb=QLineEdit()
        self.leDb.setText(self.DbPath)
        layDb.addWidget(self.leDb)
        ###btnDb
        btnChangeDb=QPushButton('浏览')
        btnChangeDb.clicked.connect(self.btnChangeDb_Clicked)
        layDb.addWidget(btnChangeDb)
        ###lblTbl
        lblTbl=QLabel('数据表：')
        layDb.addWidget(lblTbl)
        ###self.cbbTbls
        self.cbbTbls=QComboBox()
        tbls=list(map(lambda x:x[1],
                      list(filter(lambda x:x[0]=='table',
                                  self.Db.execute(
                                      'Select * From sqlite_master'
                                      ).fetchall()
                                  )
                           )
                      )
                  )
        self.cbbTbls.addItems(tbls)
        if self.CurrentTable!='' :
            self.cbbTbls.setCurrentIndex(tbls.index(self.CurrentTable))
        else:
            self.CurrentTable=tbls[0]
            self.makeTableInfo()
            self.cbbTbls.setCurrentIndex(0)
        layDb.addWidget(self.cbbTbls)
        ###lblRename
        lblRename=QLabel('重命名为：')
        layDb.addWidget(lblRename)
        ###self.leRename
        self.leRename=QLineEdit()
        self.leRename.setFixedWidth(100)
        layDb.addWidget(self.leRename)
        ###btnRename
        btnRenameTable=QPushButton('重命名')
        btnRenameTable.clicked.connect(self.btnRenameTable_Clicked)
        layDb.addWidget(btnRenameTable)
        ###btnDeleteTable
        btnDeleteTable=QPushButton('删除表')
        btnDeleteTable.clicked.connect(self.btnDeleteTable_Clicked)
        layDb.addWidget(btnDeleteTable)
        ###btnShow
        self.btnShow=QPushButton('查看表结构')
        self.btnShow.clicked.connect(self.btnShow_Clicked)
        layDb.addWidget(self.btnShow)
        ###设置TableView控件self.tv，以呈现表数据
        self.tv=QTableView()
        lay.addWidget(self.tv)
        ###self.model基本初始化
        self.model=QSqlTableModel(self,QSqlDatabase.addDatabase('QSQLITE'))
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        ###self.tv链接到数据源
        self.tv.setModel(self.model)
        ###self.model数据初始化
        self.model.database().setDatabaseName(self.DbPath)
        self.model.database().open()
        self.model.setTable(self.CurrentTable)
        self.model.select()
        self.cbbTbls.currentIndexChanged.connect(self.changeTable)
        ##layBtns
        layBtns=QHBoxLayout()
        lay.addLayout(layBtns)
        ###btnAddColumn
        btnAddColumn=QPushButton('添加列')
        btnAddColumn.setToolTip('给当前表添加列')
        btnAddColumn.clicked.connect(self.btnAddColumn_Clicked)
        layBtns.addWidget(btnAddColumn)
        ###btnDeleteColumn
        btnDeleteColumn=QPushButton('删除列')
        btnDeleteColumn.setToolTip('删除当前表的列')
        btnDeleteColumn.clicked.connect(self.btnDeleteColumn_Clicked)
        layBtns.addWidget(btnDeleteColumn)
        ###btnRenameColumn
        btnRenameColumn=QPushButton('重命名列')
        btnRenameColumn.setToolTip('重命名当前表的列')
        btnRenameColumn.clicked.connect(self.btnRenameColumn_Clicked)
        layBtns.addWidget(btnRenameColumn)
        ###btnModifyColumnType
        btnModifyColumnType=QPushButton('修改列数据类型')
        btnModifyColumnType.setToolTip('修改当前表的列的数据类型')
        btnModifyColumnType.clicked.connect(self.btnModifyColumnType_Clicked)
        layBtns.addWidget(btnModifyColumnType)
        ###btnModifyColumnConstraint
        btnModifyColumnConstraint=QPushButton('修改列约束')
        btnModifyColumnConstraint.setToolTip('修改当前表的列的约束')
        btnModifyColumnConstraint.clicked.connect(
            self.btnModifyColumnConstraint_Clicked)
        layBtns.addWidget(btnModifyColumnConstraint)
        ###btnOrderColumns
        btnOrderColumns=QPushButton('调整列顺序')
        btnOrderColumns.setToolTip('调整当前表的列的顺序')
        btnOrderColumns.clicked.connect(self.btnOrderColumns_Clicked)
        layBtns.addWidget(btnOrderColumns)
        ###btnModifyTableStruct
        btnModifyTableStruct=QPushButton('修改表结构')
        btnModifyTableStruct.setToolTip('功能：1.增加列；2.删除列；'
                                        +'3.修改列名；4.修改列类型；'
                                        +'5.修改列约束;6.调整列顺序'
                                        )
        btnModifyTableStruct.clicked.connect(self.btnModifyTableStruct_Clicked)
        layBtns.addWidget(btnModifyTableStruct)
        ###btnInsertRow
        btnInsertRow=QPushButton('插入行')
        btnInsertRow.setToolTip('将在数据表最后增加一行新记录')
        btnInsertRow.clicked.connect(self.btnInsertRow_Clicked)
        layBtns.addWidget(btnInsertRow)
        ###btnDeleteRows
        btnDeleteRows=QPushButton('删除行')
        btnDeleteRows.setToolTip('删除所有选中项所在的行')
        btnDeleteRows.clicked.connect(self.btnDeleteRows_Clicked)
        layBtns.addWidget(btnDeleteRows)
        ###btnQuery
        btnQuery=QPushButton('查询数据')
        btnQuery.setToolTip('对当前表或数据库进行查询，查询语句将被直接链接到self.model上')
        btnQuery.clicked.connect(self.btnQuery_Clicked)
        layBtns.addWidget(btnQuery)

        self.show()
        self.app.exec_()

    def __del__(self):
        #销毁多余数据库连接
        #self.Db.commit()
        self.Db.close()
    #----------------------------------------------------------------
    def makeTableInfo(self):
        #table_info=self.Db.execute('pragma table_info(%s)'%self.CurrentTable).fetchall()
        paragmastr="pragma table_info( '" + self.CurrentTable + "' ) "
        table_info=self.Db.execute(paragmastr).fetchall()
        self.columnsCount=len(table_info)
        self.columnsName=list(map(lambda x:x[1],table_info))
        self.columnsType=list(map(lambda x:x[2],table_info))
        dbinfo=self.Db.execute('select * from sqlite_master').fetchall()
        for x in dbinfo:
            if x[0]=='table' and x[1]==self.CurrentTable:
                self.sqlStr=x[4]
                break
    def DeleteColumn(self,tableName,columnName,tempName=''):
        if tempName=='':
            #tempName==''表示直接删除对应的列并提交数据库更改
            tempName=tableName+'temp'
            sqlite_master_sql="select * from sqlite_master"
            sqlite_master=self.Db.execute(sqlite_master_sql).fetchall()
            createStr=filter(lambda x:x[0]=='table' and x[1]==tableName,
                             self.Db.execute('select * from sqlite_master').fetchall())[0][4]
            createStr=','.join(filter(lambda x:x.find(columnName)==-1,createStr.split(',')))
            newColumns=','.join(map(lambda x:x[1],self.Db.execute('Pragma table_info(%s)'%tableName).fetchall()))
            #将旧表重命名为临时表名
            self.Db.execute("Alter Table %s Rename To %s"%(tableName,tempName))
            #新建删除了指定列的数据表
            self.Db.execute(createStr)
            #将旧表的数据导入新表
            self.Db.execute('Insert Into %s Select %s From %s'%
                            (tableName,newColumns,tempName))
            #删除旧表
            self.Db.execute('Drop Table %s'%tempName)
    #----------------------------------------------------------------
    def btnChangeDb_Clicked(self,event):
        pt=QFileDialog.getOpenFileName(
            caption='请选择一个sqlite数据库文件：',
            filter='sqlite数据库文件 (*.db)',
            directory=os.path.dirname(self.DbPath)
            )
        p=pt[0]
        if platform.system()=='Windows':
            p=p.replace('/','\\')
        if os.path.exists(p):
            self.DbPath=p
            self.Db=sqlite3.connect(self.DbPath)
            tbls=map(lambda x:x[1],
                 filter(lambda x:x[0]=='table',
                        self.Db.execute(
                            'Select * From sqlite_master'
                            ).fetchall()
                        )
                 )
            self.cbbTbls.currentIndexChanged.disconnect(self.changeTable)
            self.cbbTbls.clear()
            self.cbbTbls.addItems(tbls)
            self.cbbTbls.currentIndexChanged.connect(self.changeTable)
            self.CurrentTable=tbls[0]
            self.cbbTbls.setCurrentIndex(0)
            self.leDb.setText(p)
            self.model.database().setDatabaseName(self.DbPath)
            self.model.database().open()
            self.model.setTable(self.CurrentTable)
            self.model.select()
    def changeTable(self,event):
        if self.CurrentTable!=self.cbbTbls.itemText(event):
            self.CurrentTable=self.cbbTbls.itemText(event)
            self.model.setTable(self.CurrentTable)
            self.model.select()
            self.makeTableInfo()
            self.btnShow.setText('查看表结构')
    def btnDeleteTable_Clicked(self,event):
        self.Db.execute('Drop Table %s'%self.CurrentTable)
        for i in range(self.cbbTbls.count()-1,-1,-1):
            if self.cbbTbls.itemText(i)==self.CurrentTable:
                self.cbbTbls.removeItem(i)
                break
        self.CurrentTable=self.cbbTbls.itemText(0)
        self.model.setTable(self.CurrentTable)
        self.model.select()
    def btnRenameTable_Clicked(self,event):
        if self.leRename.text()!='':
            if self.leRename.text()!=self.CurrentTable:
                try:
                    self.Db.execute('Alter Table %s Rename To %s'%
                                (self.CurrentTable,self.leRename.text())
                                )
                except sqlite3.OperationalError as e:
                    if e.message=='there is already another table or index with this name: %s'%self.leRename.text():
                        QMessageBox.information(self,'错误',
                            '抱歉，本数据库中以“'+self.leRename.text()+
                            '”为名称的表或索引已经存在，无法完'+
                            '成重命名，请重新输入一个名称',
                            '知道了')
                    else:
                        QMessageBox.information(self,'错误',
                            '抱歉，可能是因表名包含非法字符，故'+
                            '无法完成重命名，请重新输入表名',
                            '知道了')
                    self.leRename.setText('')
                    return
                self.CurrentTable=self.leRename.text()
                self.cbbTbls.setItemText(self.cbbTbls.currentIndex(),
                                         self.CurrentTable
                                         )
                self.model.clear()
                self.model.setQuery(QSqlQuery(
                    'Select * From %s'%self.CurrentTable))
                self.model.select()
                self.leRename.setText('')
        else:
            QMessageBox.information(self,'注意',
                '抱歉，你还没有输入当前表要修改成的表名\n\n'+
                '请先在文本框里输入当前表要重命名成的名字，再点击我',
                '知道了')
    def btnShow_Clicked(self,event):
        if self.btnShow.text()=='查看表结构':
            self.model.setTable('')
            self.model.setQuery(QSqlQuery(
                'pragma table_info(%s)'%self.CurrentTable))
            self.model.select()
            self.btnShow.setText('查看表数据')
        else:
            self.model.setTable(self.CurrentTable)
            self.model.select()
            self.btnShow.setText('查看表结构')
    #----------------------------------------------------------------
    def btnInsertRow_Clicked(self,event):
        self.dlg_InsertRow_Values=[]
        #self.dlg
        self.dlg=QDialog()
        self.dlg.setWindowTitle('插入数据行：')
        #lay
        lay=QVBoxLayout()
        self.dlg.setLayout(lay)
        #lblprompt
        lblprompt=QLabel(
            '请参照创建此表的Sql字符串：\n'+self.sqlStr+
            '\n设置各个字段的数据：')
        lay.addWidget(lblprompt)
        #layG
        layG=QGridLayout()
        lay.addLayout(layG)
        for i in range(len(self.columnsName)):
            #lbl
            lbl=QLabel(self.columnsName[i]+'('+self.columnsType[i]+'):')
            lbl.setAlignment(Qt.AlignRight)
            layG.addWidget(lbl,i,0)
            #le
            le=QLineEdit()
            layG.addWidget(le,i,1)
            if self.columnsType[i].lower() not in self.SqliteDbTypes:
                #cbb
                cbb=QComboBox()
                cbb.addItems(self.SqliteDbTypes)
                cbb.setCurrentIndex(2)
                cbb.setToolTip(
                    '此字段的数据类型不是sqlite标准数据'+
                    '类型，请设置其存储时的使用的sqlite数据类型')
                layG.addWidget(cbb,i,2)
                self.dlg_InsertRow_Values.append((le,cbb))
            else:
                self.dlg_InsertRow_Values.append((le,self.columnsType[i]))
        layG.setColumnStretch(1,1)
        #layH
        layH=QHBoxLayout()
        lay.addLayout(layH)
        #btnOk
        btnOk=QPushButton('确定')
        btnOk.clicked.connect(self.dlg_InsertRow_btnOk_Clicked)
        layH.addWidget(btnOk)
        #btnCancel
        btnCancel=QPushButton('取消')
        btnCancel.clicked.connect(self.dlg.close)
        layH.addWidget(btnCancel)
        self.dlg.show()
    def dlg_InsertRow_btnOk_Clicked(self,event):
        sqlStr="Insert Into %s Values("%self.CurrentTable
        for item in self.dlg_InsertRow_Values:
            if item[0].text()!='':
                if type(item[1])==QComboBox:
                    print (item[0].text(),item[1].currentText())
                else:
                    print (item[0].text(),item[1])
            else:
                pass
    def btnDeleteRows_Clicked(self,event):
        rs=list(map(lambda x:x.row(),self.tv.selectedIndexes()))
        if len(rs)==0:
            QMessageBox.information(self,'提醒','请先选中至少一行，再点击此按钮！')
            return
        for i in reversed(rs):
            self.model.removeRows(i,1)
        self.model.submitAll()
    def btnQuery_Clicked(self,event):
        sqltxt,ok=QInputDialog.getText(self,'查询语句设置',
           '参照创建此表的Sql字符串：\n'+self.sqlStr+
           '\n请输入要设置到self.model的查询语句：')
        if ok:
            self.model.setTable('')
            self.model.setQuery(QSqlQuery(sqltxt))
            self.model.select()
    #----------------------------------------------------------------
    def btnAddColumn_Clicked(self,event):
        self.dlgMake_AddColumn()
    def dlgMake_AddColumn(self,lay=None):
        if lay is None:
            self.dlg=QDialog(self)
            self.dlg.setWindowTitle('添加列：')
        else:
            ##self.grpAddColumn
            self.grpAddColumn=QGroupBox('添加列：')
            self.grpAddColumn.setCheckable(True)
            self.grpAddColumn.setChecked(True)
            lay.addWidget(self.grpAddColumn)
	###layAddColumn
        layAddColumn=QVBoxLayout()
        if lay is None:
            self.dlg.setLayout(layAddColumn)
        else:
            self.grpAddColumn.setLayout(layAddColumn)
        ####self.grpAddColumn_ByCmdArgs
        self.grpAddColumn_ByCmdArgs=QGroupBox('使用参数创建列：')
        self.grpAddColumn_ByCmdArgs.setCheckable(True)
        self.grpAddColumn_ByCmdArgs.setChecked(True)
        self.PreviousChecked=0
        self.grpAddColumn_ByCmdArgs.toggled.connect(
            self.grpAddColumn_ByCmd_toggled)
        layAddColumn.addWidget(self.grpAddColumn_ByCmdArgs)
        #####layAddColumn_ByCmdArgs
        layAddColumn_ByCmdArgs=QHBoxLayout()
        self.grpAddColumn_ByCmdArgs.setLayout(layAddColumn_ByCmdArgs)
        ####lblAddColumn_select
        lblAddColumn_name=QLabel('列名：')
        layAddColumn_ByCmdArgs.addWidget(lblAddColumn_name)
        ####self.leAddColumn_name
        self.leAddColumn_name=QLineEdit()
        self.leAddColumn_name.setFixedWidth(100)
        layAddColumn_ByCmdArgs.addWidget(self.leAddColumn_name)
        ######lblAddColumn_type
        lblAddColumn_type=QLabel('类型：')
        layAddColumn_ByCmdArgs.addWidget(lblAddColumn_type)
        ######self.cbbAddColumn_type
        self.cbbAddColumn_type=QComboBox()
        self.cbbAddColumn_type.addItems(self.SqliteDbTypes)
        self.cbbAddColumn_type.setCurrentIndex(0)
        self.cbbAddColumn_type.setEditable(True)
        layAddColumn_ByCmdArgs.addWidget(self.cbbAddColumn_type)
        ######lblAddColumn_constraint
        lblAddColumn_constraint=QLabel('约束字符串：')
        layAddColumn_ByCmdArgs.addWidget(lblAddColumn_constraint)
        ######self.leAddColumn_constraint
        self.leAddColumn_constraint=QLineEdit()
        layAddColumn_ByCmdArgs.addWidget(self.leAddColumn_constraint)
        ####self.grpAddColumn_ByCmdStr
        self.grpAddColumn_ByCmdStr=QGroupBox('使用sql字符串创建列：')
        self.grpAddColumn_ByCmdStr.setCheckable(True)
        self.grpAddColumn_ByCmdStr.setChecked(False)
        self.grpAddColumn_ByCmdStr.toggled.connect(
            self.grpAddColumn_ByCmd_toggled)
        layAddColumn.addWidget(self.grpAddColumn_ByCmdStr)
        #####layAddColumn_ByCmdStr
        layAddColumn_ByCmdStr=QHBoxLayout()
        self.grpAddColumn_ByCmdStr.setLayout(layAddColumn_ByCmdStr)
        ######lblAddColumn_cmdstr
        lblAddColumn_cmdstr=QLabel('用来增加列的部分或完整Sql字符串：')
        layAddColumn_ByCmdStr.addWidget(lblAddColumn_cmdstr)
        ######self.leAddColumn_cmdstr
        self.leAddColumn_cmdstr=QLineEdit()
        layAddColumn_ByCmdStr.addWidget(self.leAddColumn_cmdstr)
        if lay is None:
            self.dlg.show()
    def grpAddColumn_ByCmd_toggled(self,event):
        if self.PreviousChecked==0:
            self.grpAddColumn_ByCmdStr.setChecked(True)
            self.grpAddColumn_ByCmdArgs.setChecked(False)
            self.PreviousChecked=1
        else:
            self.grpAddColumn_ByCmdArgs.setChecked(True)
            self.grpAddColumn_ByCmdStr.setChecked(False)
            self.PreviousChecked=0
    #----------------------------------------------------------------
    def btnDeleteColumn_Clicked(self,event):
        self.dlgMake_DeleteColumn()
    def dlgMake_DeleteColumn(self,lay=None):
        if lay is None:
            self.dlg=QDialog(self)
            self.dlg.setWindowTitle('删除列：')
        else:
            ##self.grpDeleteColumn
            self.grpDeleteColumn=QGroupBox('删除列：')
            self.grpDeleteColumn.setCheckable(True)
            self.grpDeleteColumn.setChecked(False)
            lay.addWidget(self.grpDeleteColumn)
        ###layDeleteColumn
        layDeleteColumn=QHBoxLayout()
        if lay is None:
            self.dlg.setLayout(layDeleteColumn)
        else:
            self.grpDeleteColumn.setLayout(layDeleteColumn)
        ###layColumnList
        layColumnList=QVBoxLayout()
        layDeleteColumn.addLayout(layColumnList)
        ####lblDeleteColumn
        lblDeleteColumn=QLabel('原有的所有列：')
        layColumnList.addWidget(lblDeleteColumn)
        ####self.lstColumnList
        self.lstColumnList=QListWidget()
        self.lstColumnList.addItems(self.columnsName)
        self.lstColumnList.setFixedWidth(150)
        layColumnList.addWidget(self.lstColumnList)
        ###layDeleteBtns
        layDeleteBtns=QVBoxLayout()
        layDeleteColumn.addLayout(layDeleteBtns)
        ####btnDeleteColumn_Store
        btnDeleteColumn_Store=QPushButton('>>')
        btnDeleteColumn_Store.setFixedWidth(50)
        layDeleteBtns.addWidget(btnDeleteColumn_Store)
        ####btnDeleteColumn_Unstore
        btnDeleteColumn_Unstore=QPushButton('<<')
        btnDeleteColumn_Unstore.setFixedWidth(50)
        layDeleteBtns.addWidget(btnDeleteColumn_Unstore)
        ###layColumnsToDelete
        layColumnsToDelete=QVBoxLayout()
        layDeleteColumn.addLayout(layColumnsToDelete)
        ####lblColumnsToDelete
        lblColumnsToDelete=QLabel('要删除的列：')
        layColumnsToDelete.addWidget(lblColumnsToDelete)
        ####self.lstColumnsToDelete
        self.lstColumnsToDelete=QListWidget()
        self.lstColumnsToDelete.setFixedWidth(150)
        layColumnsToDelete.addWidget(self.lstColumnsToDelete)
        if lay is None:
            self.dlg.show()
    #----------------------------------------------------------------
    def btnRenameColumn_Clicked(self,event):
        self.dlgMake_RenameColumn()
    def dlgMake_RenameColumn(self,lay=None):
        if lay is None:
            self.dlg=QDialog(self)
            self.dlg.setWindowTitle('重命名列：')
        else:
            ##self.grpRenameColumn
            self.grpRenameColumn=QGroupBox('重命名列：')
            self.grpRenameColumn.setCheckable(True)
            self.grpRenameColumn.setChecked(False)
            lay.addWidget(self.grpRenameColumn)
        ###layRenameColumn
        layRenameColumn=QHBoxLayout()
        if lay is None:
            self.dlg.setLayout(layRenameColumn)
        else:
            self.grpRenameColumn.setLayout(layRenameColumn)
        ####lblRenameColumn_select
        lblRenameColumn_select=QLabel('选择列：')
        layRenameColumn.addWidget(lblRenameColumn_select)
        ####self.cbbRenameColumn_select
        self.cbbRenameColumn_select=QComboBox()
        self.cbbRenameColumn_select.addItems(self.columnsName)
        layRenameColumn.addWidget(self.cbbRenameColumn_select)
        ####lblRenameColumn_renameto
        lblRenameColumn_renameto=QLabel('重命名为：')
        layRenameColumn.addWidget(lblRenameColumn_renameto)
        ####self.leRenameColumn_renameto
        self.leRenameColumn_renameto=QLineEdit()
        self.leRenameColumn_renameto.setFixedWidth(80)
        layRenameColumn.addWidget(self.leRenameColumn_renameto)
        ####btnRenameColumn_Store
        btnRenameColumn_Store=QPushButton('标记 >>')
        layRenameColumn.addWidget(btnRenameColumn_Store)
        ####self.cbbRenameColumn_Store
        self.cbbRenameColumn_Store=QComboBox()
        layRenameColumn.addWidget(self.cbbRenameColumn_Store,1)
        if lay is None:
            self.dlg.show()
    #----------------------------------------------------------------
    def btnModifyColumnType_Clicked(self,event):
        self.dlgMake_ModifyColumnType()
    def dlgMake_ModifyColumnType(self,lay=None):
        if lay is None:
            self.dlg=QDialog(self)
            self.dlg.setWindowTitle('修改列数据类型：')
        else:
            ##self.grpModifyColumnType
            self.grpModifyColumnType=QGroupBox('修改列数据类型：')
            self.grpModifyColumnType.setCheckable(True)
            self.grpModifyColumnType.setChecked(False)
            lay.addWidget(self.grpModifyColumnType)
        ###layModifyColumnType
        layModifyColumnType=QHBoxLayout()
        if lay is None:
            self.dlg.setLayout(layModifyColumnType)
        else:
            self.grpModifyColumnType.setLayout(layModifyColumnType)
        ####lblModifyColumnType_select
        lblModifyColumnType_select=QLabel('选择列：')
        layModifyColumnType.addWidget(lblModifyColumnType_select)
        ####self.cbbModifyColumnType_select
        self.cbbModifyColumnType_select=QComboBox()
        self.cbbModifyColumnType_select.addItems(self.columnsName)
        layModifyColumnType.addWidget(self.cbbModifyColumnType_select)
        ####lblModifyColumnType_modifyto
        lblModifyColumnType_modifyto=QLabel('改类型为：')
        layModifyColumnType.addWidget(lblModifyColumnType_modifyto)
        ####self.cbbModifyColumnType_modifyto
        self.cbbModifyColumnType_modifyto=QComboBox()
        self.cbbModifyColumnType_modifyto.setEditable(True)
        self.cbbModifyColumnType_modifyto.addItems(self.SqliteDbTypes)
        self.cbbModifyColumnType_modifyto.setCurrentIndex(2)
        self.cbbModifyColumnType_modifyto.setFixedWidth(80)
        layModifyColumnType.addWidget(self.cbbModifyColumnType_modifyto)
        ####btnModifyColumnType_Store
        btnModifyColumnType_Store=QPushButton('标记 >>')
        layModifyColumnType.addWidget(btnModifyColumnType_Store)
        ####self.cbbModifyColumnType_Store
        self.cbbModifyColumnType_Store=QComboBox()
        layModifyColumnType.addWidget(self.cbbModifyColumnType_Store,1)
        if lay is None:
            self.dlg.show()
    #----------------------------------------------------------------
    def btnModifyColumnConstraint_Clicked(self,event):
        self.dlgMake_ModifyColumnConstraint()
    def dlgMake_ModifyColumnConstraint(self,lay=None):
        if lay is None:
            self.dlg=QDialog(self)
            self.dlg.setWindowTitle('修改列约束：')
        else:
            ##self.grpModifyColumnConstraint
            self.grpModifyColumnConstraint=QGroupBox('修改列约束：')
            self.grpModifyColumnConstraint.setCheckable(True)
            self.grpModifyColumnConstraint.setChecked(False)
            lay.addWidget(self.grpModifyColumnConstraint)
        ###layModifyColumnConstraint
        layModifyColumnConstraint=QHBoxLayout()
        if lay is None:
            self.dlg.setLayout(layModifyColumnConstraint)
        else:
            self.grpModifyColumnConstraint.setLayout(layModifyColumnConstraint)
        ####lblModifyColumnConstraint_select
        lblModifyColumnConstraint_select=QLabel('选择列：')
        layModifyColumnConstraint.addWidget(lblModifyColumnConstraint_select)
        ####self.cbbModifyColumnConstraint_select
        self.cbbModifyColumnConstraint_select=QComboBox()
        self.cbbModifyColumnConstraint_select.addItems(self.columnsName)
        layModifyColumnConstraint.addWidget(self.cbbModifyColumnConstraint_select)
        ####lblModifyColumnConstraint_modifyto
        lblModifyColumnConstraint_modifyto=QLabel('约束改为：')
        layModifyColumnConstraint.addWidget(lblModifyColumnConstraint_modifyto)
        ####self.leModifyColumnConstraint_modifyto
        self.leModifyColumnConstraint_modifyto=QLineEdit()
        self.leModifyColumnConstraint_modifyto.setFixedWidth(80)
        layModifyColumnConstraint.addWidget(self.leModifyColumnConstraint_modifyto)
        ####btnModifyColumnConstraint_Store
        btnModifyColumnConstraint_Store=QPushButton('标记 >>')
        layModifyColumnConstraint.addWidget(btnModifyColumnConstraint_Store)
        ####self.cbbModifyColumnConstraint_Store
        self.cbbModifyColumnConstraint_Store=QComboBox()
        layModifyColumnConstraint.addWidget(self.cbbModifyColumnConstraint_Store,1)
        if lay is None:
            self.dlg.show()
    #----------------------------------------------------------------
    def btnOrderColumns_Clicked(self,event):
        self.dlgMake_OrderColumns()
    def dlgMake_OrderColumns(self,lay=None):
        if lay is None:
            self.dlg=QDialog(self)
            self.dlg.setWindowTitle('调整列顺序：')
        else:
            ##self.grpAdjustColumnOrder
            self.grpAdjustColumnOrder=QGroupBox('调整列顺序：')
            self.grpAdjustColumnOrder.setCheckable(True)
            self.grpAdjustColumnOrder.setChecked(False)
            lay.addWidget(self.grpAdjustColumnOrder)
        ###layAdjustColumnOrder
        layAdjustColumnOrder=QVBoxLayout()
        if lay is None:
            self.dlg.setLayout(layAdjustColumnOrder)
        else:
            self.grpAdjustColumnOrder.setLayout(layAdjustColumnOrder)
        ####lblAdjustColumnOrder
        lblAdjustColumnOrder=QLabel('请调整列顺序：')
        layAdjustColumnOrder.addWidget(lblAdjustColumnOrder)
        ####self.lstAdjustColumnOrder
        self.lstAdjustColumnOrder=QListWidget()
        self.lstAdjustColumnOrder.addItems(self.columnsName)
        self.lstAdjustColumnOrder.setFixedWidth(150)
        layAdjustColumnOrder.addWidget(self.lstAdjustColumnOrder)
        if lay is None:
            self.dlg.setFixedWidth(175)
            self.dlg.show()
    #----------------------------------------------------------------
    def btnModifyTableStruct_Clicked(self,event):
        self.dlg=QDialog(self)
        self.dlg.setWindowTitle(self.CurrentTable+'表结构修改：')
        self.dlg.setWindowFlags(Qt.Window|
                           Qt.MSWindowsFixedSizeDialogHint
                           )
        #lay
        lay=QVBoxLayout()
        self.dlgMake_AddColumn(lay)
        self.dlgMake_RenameColumn(lay)
        self.dlgMake_ModifyColumnType(lay)
        self.dlgMake_ModifyColumnConstraint(lay)
        #layLists
        layLists=QHBoxLayout()
        lay.addLayout(layLists)
        self.dlgMake_DeleteColumn(layLists)
        self.dlgMake_OrderColumns(layLists)
        ##layBtns
        layBtns=QHBoxLayout()
        lay.addLayout(layBtns)
        ##btnOk
        btnOk=QPushButton('提交修改')
        btnOk.clicked.connect(self.btnOk_Clicked)
        layBtns.addWidget(btnOk)
        ##btnCancel
        btnCancel=QPushButton('放弃修改')
        btnCancel.clicked.connect(self.btnCancel_Clicked)
        layBtns.addWidget(btnCancel)

        self.dlg.setLayout(lay)
        self.dlg.open()
    def btnOk_Clicked(self,event):
        #do something here
        self.dlg.close()
    def btnCancel_Clicked(self,event):
        self.dlg.close()

if __name__=='__main__':
    if len(sys.argv)==1:
        SqliteDbTableEditer('test.db')
    if len(sys.argv)==2:
        if os.path.exists(os.path.abspath(sys.argv[1])):
            SqliteDbTableEditer(sys.argv[1])
    if len(sys.argv)==3:
       if os.path.exists(os.path.abspath(sys.argv[1])):
            SqliteDbTableEditer(sys.argv[1],sys.argv[2])
