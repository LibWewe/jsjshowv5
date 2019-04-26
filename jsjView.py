#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: jsjView.py
@version: v1.0 
@author: WeWe 
@time: 2018/07/06 11:14
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""
import jsjshow
from icon.icon import Back_ico, Close_ico, endPage1_ico, Eye_ico, \
    firstPage1_ico, lastPage2_ico, prevPage2_ico, \
    Printer_ico, refresh1_ico, table2_png
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QLineEdit
from PyQt5.QtGui import QFont, QRegExpValidator, QImage, QPainter, QPen, QBrush, QPixmap
from PyQt5.QtCore import Qt, QRect, QSize, QTimer, QRegExp, QPoint, QDir
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
import loginWin
import machinWin
import wearTableWin
import wearCardWin
import newCardWin
import mainWin
import sys, os
import base64
import time
import math
import qrcode
from PIL import Image
import datetime

BASE_DIRS = os.path.dirname(__file__)


class loginView(QtWidgets.QWidget, loginWin.Ui_Form):
    def __init__(self):
        """

        """
        super(loginView, self).__init__()
        self.setupUi(self)
        self.account.setPlaceholderText("用户名")
        self.password.setPlaceholderText("密  码")


class machineView(QtWidgets.QMainWindow, machinWin.Ui_Form):
    def __init__(self):
        """

        """
        super(machineView, self).__init__()
        self.setupUi(self)

        self.toolbar = QtWidgets.QToolBar("Navigation")
        self.addToolBar(self.toolbar)
        self.refreshAct = QtWidgets.QAction(QtGui.QIcon("refresh1.ico"), "刷新设备列表")
        self.firstAct = QtWidgets.QAction(QtGui.QIcon("firstPage1.ico"), "查看第一页设备列表")
        self.prevAct = QtWidgets.QAction(QtGui.QIcon("prevPage2.ico"), "查看上一页设备列表")
        self.lastAct = QtWidgets.QAction(QtGui.QIcon("lastPage2.ico"), "查看下一页设备列表")
        self.endAct = QtWidgets.QAction(QtGui.QIcon("endPage1.ico"), "查看最后一页设备列表")
        self.accountLable = QtWidgets.QLabel()
        self.accountLable.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                        self.accountLable.sizePolicy().verticalPolicy())
        self.accountLable.setText("")
        self.accountLable.setAlignment(Qt.AlignCenter)  # 设置字体居中
        self.timeLable = QtWidgets.QLabel()
        self.timeLable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, self.timeLable.sizePolicy().verticalPolicy())
        self.timeLable.setText("")
        self.timeLable.setAlignment(Qt.AlignCenter)
        self.exitAct = QtWidgets.QAction(QtGui.QIcon("Close.ico"), "退出程序")
        self.toolbar.addAction(self.refreshAct)
        self.toolbar.addAction(self.firstAct)
        self.toolbar.addAction(self.prevAct)
        self.toolbar.addAction(self.lastAct)
        self.toolbar.addAction(self.endAct)
        self.toolbar.addWidget(self.accountLable)
        self.toolbar.addWidget(self.timeLable)
        self.toolbar.addAction(self.exitAct)
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.accountLable.setText("  " + "，您好")
        self.timeLable.setText(str(nowtime))
        lableFont = QFont("Roman times", 12, QFont.Bold)
        self.accountLable.setFont(lableFont)
        self.timeLable.setFont(lableFont)
        self.accountLable.setStyleSheet("color:blue")
        self.timeLable.setStyleSheet("color:blue")

        self.machineTable.setHorizontalHeaderLabels(["序号", "设备名称", "厂区名称", "状态"])
        self.machineTable.verticalHeader().setVisible(False)
        rect = self.machineTable.rect()
        self.machineTable.setColumnWidth(0, 50)
        self.machineTable.setColumnWidth(1, (rect.width() - 50 * 2) / 2)
        self.machineTable.setColumnWidth(2, (rect.width() - 50 * 2) / 2)
        self.machineTable.setColumnWidth(3, 50)


class wearTableView(QtWidgets.QMainWindow, wearTableWin.Ui_Form):
    def __init__(self):
        """

        """
        super(wearTableView, self).__init__()
        self.setupUi(self)
        self.toolbar = QtWidgets.QToolBar("Navigation")
        self.addToolBar(self.toolbar)
        self.refreshAct = QtWidgets.QAction(QtGui.QIcon("refresh1.ico"), "刷新织轴卡列表")
        self.firstAct = QtWidgets.QAction(QtGui.QIcon("firstPage1.ico"), "查看第一页织轴卡列表")
        self.prevAct = QtWidgets.QAction(QtGui.QIcon("prevPage2.ico"), "查看上一页织轴卡列表")
        self.lastAct = QtWidgets.QAction(QtGui.QIcon("lastPage2.ico"), "查看下一页织轴卡列表")
        self.endAct = QtWidgets.QAction(QtGui.QIcon("endPage1.ico"), "查看最后一页织轴卡列表")
        self.lookLatestAct = QtWidgets.QAction(QtGui.QIcon("Eye.ico"), "查看最新织轴卡")

        self.lableFont = QFont("Roman times", 12, QFont.Bold)
        self.timeLable = QtWidgets.QLabel()
        self.timeLable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, self.timeLable.sizePolicy().verticalPolicy())
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.timeLable.setText(str(self.nowtime))
        self.timeLable.setFont(self.lableFont)
        self.timeLable.setStyleSheet("color:blue")
        self.timeLable.setAlignment(Qt.AlignCenter)

        self.curPage = 0
        self.curPageEdit = QLineEdit()
        validator = QRegExpValidator(QRegExp("\d+"))
        self.curPageEdit.setValidator(validator)  # 设置只能输入数字
        self.curPageEdit.setText(str(self.curPage))
        self.curPageEdit.setMaximumSize(QSize(40, 20))
        self.curPageEdit.setFont(self.lableFont)
        self.curPageEdit.setStyleSheet("color:blue")
        self.curPageEdit.setAlignment(Qt.AlignCenter)

        self.totalPage = 0
        self.totalPageLable = QtWidgets.QLabel()
        self.totalPageLable.setText("/" + str(self.totalPage) + "(共" + str(self.totalPage) + "页)")
        self.totalPageLable.setFont(self.lableFont)
        self.totalPageLable.setStyleSheet("color:blue")
        self.totalPageLable.setAlignment(Qt.AlignCenter)

        self.backAct = QtWidgets.QAction(QtGui.QIcon("Back.ico"), "返回设备列表")

        self.toolbar.addAction(self.refreshAct)
        self.toolbar.addAction(self.firstAct)
        self.toolbar.addAction(self.prevAct)
        self.toolbar.addWidget(self.curPageEdit)
        self.toolbar.addWidget(self.totalPageLable)
        self.toolbar.addAction(self.lastAct)
        self.toolbar.addAction(self.endAct)
        self.toolbar.addAction(self.lookLatestAct)
        self.toolbar.addWidget(self.timeLable)
        self.toolbar.addAction(self.backAct)
        self.wearTable.setHorizontalHeaderLabels(["序号", "设备名称", "所属厂区", "洛轴时间"])
        self.wearTable.verticalHeader().setVisible(False)  # 隐藏纵向表头
        rect = self.wearTable.rect()
        self.wearTable.setColumnWidth(0, 50)
        self.wearTable.setColumnWidth(1, (rect.width() - 50) / 3)
        self.wearTable.setColumnWidth(2, (rect.width() - 50) / 3)
        self.wearTable.setColumnWidth(3, (rect.width() - 50) / 3)


class wearCardView(QtWidgets.QMainWindow, wearCardWin.Ui_Form):
    def __init__(self):
        super(wearCardView, self).__init__()
        self.setupUi(self)

        self.wearCardID = 0
        self.toolbar = QtWidgets.QToolBar("Navigation")
        self.addToolBar(self.toolbar)
        self.refreshAct = QtWidgets.QAction(QtGui.QIcon("refresh1.ico"), "刷新当前织轴卡")
        self.printAct = QtWidgets.QAction(QtGui.QIcon("Printer.ico"), "打印当前织轴卡")
        self.backAct = QtWidgets.QAction(QtGui.QIcon("Back.ico"), "返回织轴卡列表")

        self.lableFont = QFont("Roman times", 12, QFont.Bold)
        self.timeLable = QtWidgets.QLabel()
        self.timeLable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, self.timeLable.sizePolicy().verticalPolicy())
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.timeLable.setText(str(self.nowtime))
        self.timeLable.setFont(self.lableFont)
        self.timeLable.setStyleSheet("color:blue")
        self.timeLable.setAlignment(Qt.AlignCenter)

        self.toolbar.addAction(self.refreshAct)
        self.toolbar.addAction(self.printAct)
        self.toolbar.addWidget(self.timeLable)
        self.toolbar.addAction(self.backAct)
        self.wearCard.horizontalHeader().setVisible(False)  # 隐藏横向表头
        self.wearCard.verticalHeader().setVisible(False)  # 隐藏纵向表头
        rect = self.wearCard.rect()
        self.wearCard.setColumnWidth(0, 200)
        self.wearCard.setColumnWidth(1, (rect.width() - 200))
        titlestr = ["设备名称", "机台号", "所属厂区", "设备型号", "纱支", "轴号", "班次",
                    "挡车工姓名", "班长姓名", "匹数", "纱长", "纱长详情", "品种", "落轴时间"]
        for i in range(0, 14):
            self.wearCard.setItem(i, 0, QTableWidgetItem(titlestr[i]))


class newCardView(QtWidgets.QMainWindow, newCardWin.Ui_Form):
    def __init__(self):
        super(newCardView, self).__init__()
        self.setupUi(self)
        self.wearCardID = 0
        self.toolbar = QtWidgets.QToolBar("Navigation")
        self.addToolBar(self.toolbar)
        self.refreshAct = QtWidgets.QAction(QtGui.QIcon("refresh1.ico"), "刷新最新织轴卡")
        self.printAct = QtWidgets.QAction(QtGui.QIcon("Printer.ico"), "打印当前织轴卡")
        self.backAct = QtWidgets.QAction(QtGui.QIcon("Back.ico"), "返回织轴卡列表")

        self.lableFont = QFont("Roman times", 12, QFont.Bold)
        self.timeLable = QtWidgets.QLabel()
        self.timeLable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, self.timeLable.sizePolicy().verticalPolicy())
        self.nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.timeLable.setText(str(self.nowtime))
        self.timeLable.setFont(self.lableFont)
        self.timeLable.setStyleSheet("color:blue")
        self.timeLable.setAlignment(Qt.AlignCenter)

        self.toolbar.addAction(self.refreshAct)
        self.toolbar.addAction(self.printAct)
        self.toolbar.addWidget(self.timeLable)
        self.toolbar.addAction(self.backAct)
        self.wearCard.horizontalHeader().setVisible(False)  # 隐藏横向表头
        self.wearCard.verticalHeader().setVisible(False)  # 隐藏纵向表头
        rect = self.wearCard.rect()
        self.wearCard.setColumnWidth(0, 200)
        self.wearCard.setColumnWidth(1, (rect.width() - 200))
        titlestr = ["设备名称", "机台号", "所属厂区", "设备型号", "纱支", "轴号", "班次",
                    "挡车工姓名", "班长姓名", "匹数", "纱长", "纱长详情", "品种", "落轴时间"]
        for i in range(0, 14):
            self.wearCard.setItem(i, 0, QTableWidgetItem(titlestr[i]))


class mainView(QtWidgets.QMainWindow, mainWin.Ui_MainWindow):
    def __init__(self, jsj):
        """
        主窗口类
        :param jsj:对浆纱机云平台访问的类，提供了登陆、查看设备列表、获取织轴卡列表、获取织轴卡详情的接口
        """
        super(mainView, self).__init__()
        self.setupUi(self)
        self.statuLable = QtWidgets.QLabel()
        self.statuLable.setMinimumSize(self.statuLable.sizeHint())
        self.statuLable.setAlignment(Qt.AlignCenter)
        self.statusbar.addWidget(self.statuLable)
        self.statusbar.setStyleSheet("QStatusBar::item{border: 0px}")
        self.statuLable.setText("就绪")

        self.jsj = jsj
        self.accountStr = "jslfscz"
        self.passwordStr = "123456"
        self.maxPageSize = 15
        self.machinPageNo = 1
        self.machineTotalPage = 1
        self.curView = 1
        self.fileName = ""
        self.printer = QPrinter(QPrinter.HighResolution)

        self.loadPic()

        self.setWindowFlag(Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.loginview = loginView()
        self.loginview.password.returnPressed.connect(self.onClickedLoginBtn)
        self.loginview.account.returnPressed.connect(self.onClickedLoginBtn)
        self.loginview.loginBtn.clicked.connect(self.onClickedLoginBtn)

        self.updateTime = QTimer()
        self.updateTime.start(1000)
        self.updateTime.timeout.connect(self.onUpdateTimeOut)

        self.updateView = QTimer()
        self.updateView.start(20000)
        self.updateView.timeout.connect(self.onUpdateViewOut)

        self.machineview = machineView()
        self.machineview.refreshAct.triggered.connect(self.onTriggeredRefreshAct_m)
        self.machineview.firstAct.triggered.connect(self.onTriggeredFirstAct_m)
        self.machineview.prevAct.triggered.connect(self.onTriggeredPrevAct_m)
        self.machineview.lastAct.triggered.connect(self.onTriggeredLastAct_m)
        self.machineview.endAct.triggered.connect(self.onTriggeredEndAct_m)
        self.machineview.exitAct.triggered.connect(self.onTriggeredExitAct_m)
        self.machineview.machineTable.itemDoubleClicked['QTableWidgetItem*'].connect(self.onDoubleClickedMachineList)

        self.wearlistview = wearTableView()
        self.wearlistview.refreshAct.triggered.connect(self.onTriggeredRefreshAct_w)
        self.wearlistview.firstAct.triggered.connect(self.onTriggeredFirstAct_w)
        self.wearlistview.prevAct.triggered.connect(self.onTriggeredPrevAct_w)
        self.wearlistview.curPageEdit.returnPressed.connect(self.onPressedCurPageEdit_W)
        self.wearlistview.lastAct.triggered.connect(self.onTriggeredLastAct_w)
        self.wearlistview.endAct.triggered.connect(self.onTriggeredEndAct_w)
        self.wearlistview.lookLatestAct.triggered.connect(self.onTriggeredLookLatestAct_w)
        self.wearlistview.backAct.triggered.connect(self.onTriggeredBackAct_w)
        self.wearlistview.wearTable.itemDoubleClicked['QTableWidgetItem*'].connect(self.onDoubleClickedWearList)

        self.wearcardview = wearCardView()
        self.wearcardview.refreshAct.triggered.connect(self.onTriggeredRefreshAct_c)
        self.wearcardview.printAct.triggered.connect(self.onTriggeredPrintAct_c)
        self.wearcardview.backAct.triggered.connect(self.onTriggeredBackAct_c)

        self.newcardview = newCardView()
        self.newcardview.refreshAct.triggered.connect(self.onTriggeredRefreshAct_n)
        self.newcardview.printAct.triggered.connect(self.onTriggeredPrintAct_n)
        self.newcardview.backAct.triggered.connect(self.onTriggeredBackAct_n)
        files = ["Back.ico", "Close.ico", "endPage1.ico", "Eye.ico", "firstPage1.ico",
                 "lastPage2.ico", "prevPage2.ico", "Printer.ico", "refresh1.ico"]
        for i in files:
            os.remove(i)
        self.loginshow()

    def loadPic(self):
        """
        用于加载图标及图片，方便打包后获取图标及图片
        :return: 无
        """
        with open("Back.ico", "wb") as BackIco:
            BackIco.write(base64.b64decode(Back_ico))
        with open("Close.ico", "wb") as CloseIco:
            CloseIco.write(base64.b64decode(Close_ico))
        with open("endPage1.ico", "wb") as endPage1Ico:
            endPage1Ico.write(base64.b64decode(endPage1_ico))
        with open("Eye.ico", "wb") as EyeIco:
            EyeIco.write(base64.b64decode(Eye_ico))
        with open("firstPage1.ico", "wb") as firstPage1Ico:
            firstPage1Ico.write(base64.b64decode(firstPage1_ico))
        with open("lastPage2.ico", "wb") as lastPage2Ico:
            lastPage2Ico.write(base64.b64decode(lastPage2_ico))
        with open("prevPage2.ico", "wb") as prevPage2Ico:
            prevPage2Ico.write(base64.b64decode(prevPage2_ico))
        with open("Printer.ico", "wb") as PrinterIco:
            PrinterIco.write(base64.b64decode(Printer_ico))
        with open("refresh1.ico", "wb") as refresh1Ico:
            refresh1Ico.write(base64.b64decode(refresh1_ico))

    def loginshow(self):
        """
        显示登陆窗口
        :return:无
        """
        # self.loginGrid.addWidget(self.loginview)
        self.loginview.show()
        self.loginview.account.setText(self.accountStr)
        self.loginview.password.setText(self.passwordStr)
        self.curView = 1

    def onClickedLoginBtn(self):
        """
        单击登陆按钮的槽函数
        :return:
        """
        self.accountStr = self.loginview.account.text()
        self.passwordStr = self.loginview.password.text()
        ret = self.jsj.login(self.accountStr, self.passwordStr)
        if ret == 0:
            self.show()
            self.machineshow()
            self.loginview.close()
        elif ret == -1:
            QMessageBox.warning(self, "登陆提示", self.jsj.message + "      ", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "登陆提示", "登录失败，请检查网络是否可用!    ", QMessageBox.Ok, QMessageBox.Ok)

    def onUpdateTimeOut(self):
        """
        动态更新窗口上显示的系统时间,时间间隔1秒
        :return: 无
        """
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        if self.curView == 2:
            self.machineview.timeLable.setText(str(nowtime))
        if self.curView == 3:
            self.wearlistview.timeLable.setText(str(nowtime))
        if self.curView == 4:
            self.wearcardview.timeLable.setText(str(nowtime))
        if self.curView == 5:
            self.newcardview.timeLable.setText(str(nowtime))

    def onUpdateViewOut(self):
        """
        动态更新窗口现实的数据，刷新间隔20秒
        :return:
        """
        if self.curView == 2:
            self.onTriggeredRefreshAct_m()
        if self.curView == 3:
            self.onTriggeredRefreshAct_w()
        if self.curView == 4:
            self.onTriggeredRefreshAct_c()
        if self.curView == 5:
            self.onTriggeredRefreshAct_n()

    def getMachineData(self, pageNo=1):
        """
        获取设备列表数据
        :param pageNo: 设备列表中的第几页
        :return: 0:成功获取数据 ；-1：掉线，需重新登录；-2：网络异常
        """
        ret = self.jsj.machineList(pageNo=pageNo, pageSize=self.maxPageSize)
        if ret == 0:
            data = self.jsj.machineData
            self.machinListData = data["data"]
            return 0
        elif ret == -1:
            QMessageBox.warning(self, "提示", self.jsj.message + "\n由于网络原因导致账号离线，请重启软件并登陆", QMessageBox.Ok,
                                QMessageBox.Ok)
            return -1
        else:
            self.curView = 0
            if QMessageBox.warning(self, "提示", "数据获取失败，请检查网络是否可用!    ",
                                   QMessageBox.Ok, QMessageBox.Ok) == QMessageBox.Ok:
                self.machineview.close()
                self.hide()
                self.loginshow()
                return -2

    def machineshow(self):
        """
        用于显示设备列表界面，并获取设备列表数据
        :return:无
        """
        self.showGrid.addWidget(self.machineview)
        self.machineview.show()
        self.curView = 2
        self.setWindowTitle("设备列表")
        self.machineview.accountLable.setText(self.accountStr + "，您好")
        ret = self.getMachineData(pageNo=1)
        if ret == 0:
            self.machinPageNo = 1
            self.machinlist()

    def machinlist(self):
        """
        将设备列表数据显示到listWidget中
        :return: 无
        """
        # print(self.machinListData)
        self.machinPageNo = self.machinListData["pageNo"]
        total = self.machinListData["total"]
        self.machineTotalPage = math.ceil(total / self.maxPageSize)
        if total < self.maxPageSize:
            maxRow = total
        else:
            if self.machinPageNo == self.machineTotalPage:
                maxRow = total - (self.machineTotalPage - 1) * self.maxPageSize
            else:
                maxRow = self.maxPageSize
        for j in range(0, self.maxPageSize):
            for k in range(0, 4):
                self.machineview.machineTable.setItem(j, k, QTableWidgetItem(""))
        for i in range(0, maxRow):
            item = QTableWidgetItem(str(i + 1))
            self.machineview.machineTable.setItem(i, 0, item)
            self.machineview.machineTable.setItem(i, 1, QTableWidgetItem(self.machinListData["rows"][i]["machineName"]))
            self.machineview.machineTable.setItem(i, 2, QTableWidgetItem(self.machinListData["rows"][i]["plantName"]))
            if self.machinListData["rows"][i]["status"] == "STATUS_ONLINE":
                self.machineview.machineTable.setItem(i, 3, QTableWidgetItem("在线"))
            elif self.machinListData["rows"][i]["status"] == "STATUS_OFFLINE":
                self.machineview.machineTable.setItem(i, 3, QTableWidgetItem("离线"))

    def onTriggeredRefreshAct_m(self):
        """
        点击刷新按钮的槽函数
        :return: 无
        """
        ret = self.getMachineData(pageNo=self.machinPageNo)
        if ret == 0:
            self.machinlist()

    def onTriggeredFirstAct_m(self):
        """

        :return:
        """
        if self.machinPageNo != 1:
            pageNo = 1
            ret = self.getMachineData(pageNo=pageNo)
            if ret == 0:
                self.machinPageNo = 1
                self.machinlist()

    def onTriggeredPrevAct_m(self):
        if self.machinPageNo > 1:
            pageNo = self.machinPageNo - 1
            ret = self.getMachineData(pageNo=pageNo)
            if ret == 0:
                self.machinPageNo -= 1
                self.machinlist()

    def onTriggeredLastAct_m(self):
        if self.machinPageNo < self.machineTotalPage:
            pageNo = self.machinPageNo + 1
            ret = self.getMachineData(pageNo=pageNo)
            if ret == 0:
                self.machinPageNo += 1
                self.machinlist()

    def onTriggeredEndAct_m(self):
        if self.machinPageNo != self.machineTotalPage:
            pageNo = self.machineTotalPage
            ret = self.getMachineData(pageNo=pageNo)
            if ret == 0:
                self.machinPageNo = self.machineTotalPage
                self.machinlist()

    def onTriggeredExitAct_m(self):
        """

        :return:
        """
        self.machineview.close()
        self.close()

    def onDoubleClickedMachineList(self, item):
        """

        :param item:
        :return:
        """
        # print(item.row(), item.column(), item.text())
        if item.text() != "":
            self.machineId = self.machinListData["rows"][item.row()]["id"]
            self.wearlistshow()

    def getWearListData(self, pageNo=1, machineId=0):
        ret = self.jsj.weaverCardList(pageNo=pageNo, pageSize=self.maxPageSize, machineId=machineId)
        if ret == 0:
            data = self.jsj.wearListData
            self.wearListData = data["data"]
            return 0
        elif ret == -1:
            QMessageBox.warning(self, "提示", self.jsj.message + "\n由于网络原因导致账号离线，请重启软件并登陆", QMessageBox.Ok,
                                QMessageBox.Ok)
            return -1
        else:
            self.curView = 0
            if QMessageBox.warning(self, "提示", "数据获取失败，请检查网络是否可用!    ",
                                   QMessageBox.Ok, QMessageBox.Ok) == QMessageBox.Ok:
                self.wearlistview.close()
                self.machineview.close()
                self.hide()
                self.loginshow()
                return -2

    def wearlistshow(self):
        """

        :param machineId:
        :return:
        """
        self.showGrid.addWidget(self.wearlistview)
        self.wearlistview.show()
        self.machineview.hide()
        self.curView = 3
        self.setWindowTitle("织轴卡列表")
        ret = self.getWearListData(pageNo=1, machineId=self.machineId)
        if ret == 0:
            self.wearlist()
            self.wearListPageNo = 1

    def wearlist(self):
        """

        :return:
        """
        # print(self.wearListData)
        self.wearlistview.curPage = self.wearListData["pageNo"]
        self.wearlistview.totalPage = math.ceil(self.wearListData["total"] / self.maxPageSize)
        self.wearlistview.curPageEdit.setText(str(self.wearlistview.curPage))
        self.wearlistview.totalPageLable.setText(
            "/" + str(self.wearlistview.totalPage) + "(共" + str(self.wearlistview.totalPage) + "页)")
        if self.wearListData["total"] < self.maxPageSize:
            maxRow = self.wearListData["total"]
        else:
            if self.wearlistview.curPage == self.wearlistview.totalPage:
                maxRow = self.wearListData["total"] - (self.wearlistview.totalPage - 1) * self.maxPageSize
            else:
                maxRow = self.maxPageSize
        for j in range(0, self.maxPageSize):
            for k in range(0, 4):
                self.wearlistview.wearTable.setItem(j, k, QTableWidgetItem(""))
        for i in range(0, maxRow):
            self.wearlistview.wearTable.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.wearlistview.wearTable.setItem(i, 1, QTableWidgetItem(self.wearListData["rows"][i]["machineName"]))
            self.wearlistview.wearTable.setItem(i, 2, QTableWidgetItem(self.wearListData["rows"][i]["plantName"]))
            timestamp = int(self.wearListData["rows"][i]["gmtDoff"])
            timearray = time.localtime(timestamp / 1000)
            gmtDoff = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
            self.wearlistview.wearTable.setItem(i, 3, QTableWidgetItem(str(gmtDoff)))

    def onTriggeredRefreshAct_w(self):
        pageNo = self.wearlistview.curPage
        ret = self.getWearListData(pageNo=pageNo, machineId=self.machineId)
        if ret == 0:
            self.wearlist()

    def onTriggeredFirstAct_w(self):
        if self.wearlistview.curPage != 1:
            ret = self.getWearListData(pageNo=1, machineId=self.machineId)
            if ret == 0:
                self.wearlist()

    def onTriggeredPrevAct_w(self):
        if self.wearlistview.curPage > 1:
            ret = self.getWearListData(pageNo=self.wearlistview.curPage - 1, machineId=self.machineId)
            if ret == 0:
                self.wearlist()

    def onPressedCurPageEdit_W(self):
        pageNo = int(self.wearlistview.curPageEdit.text())
        if pageNo > self.wearlistview.totalPage:
            pageNo = self.wearlistview.totalPage
        if pageNo < 1:
            pageNo = 1
        ret = self.getWearListData(pageNo=pageNo, machineId=self.machineId)
        if ret == 0:
            self.wearlist()

    def onTriggeredLastAct_w(self):
        if self.wearlistview.curPage < self.wearlistview.totalPage:
            ret = self.getWearListData(pageNo=self.wearlistview.curPage + 1, machineId=self.machineId)
            if ret == 0:
                self.wearlist()

    def onTriggeredEndAct_w(self):
        if self.wearlistview.curPage != self.wearlistview.totalPage:
            ret = self.getWearListData(pageNo=self.wearlistview.totalPage, machineId=self.machineId)
            if ret == 0:
                self.wearlist()

    def onTriggeredLookLatestAct_w(self):
        self.newCardShow()

    def onTriggeredBackAct_w(self):
        self.machineview.show()
        self.wearlistview.close()
        self.setWindowTitle("设备列表")
        self.curView = 2

    def onDoubleClickedWearList(self, item):
        # print(item.row(), item.column(), item.text())
        if item.text() != "":
            wearCardID = self.wearListData["rows"][item.row()]["id"]
            self.wearCardShow(wearCardID)

    def getWearCardData(self, wearCardID):
        if self.wearcardview.wearCardID != wearCardID:
            self.wearcardview.wearCardID = wearCardID
        ret = self.jsj.weaverCard(self.wearcardview.wearCardID)
        if ret == 0:
            data = self.jsj.wearCardData
            self.wearCardData = data["data"]
            return 0
        elif ret == -1:
            QMessageBox.warning(self, "提示", self.jsj.message + "\n由于网络原因导致账号离线，请重启软件并登陆", QMessageBox.Ok,
                                QMessageBox.Ok)
            return -1
        else:
            temp = self.curView
            self.curView = 0
            if QMessageBox.warning(self, "提示", "数据获取失败，请检查网络是否可用!    ",
                                   QMessageBox.Ok, QMessageBox.Ok) == QMessageBox.Ok:
                if temp == 4:
                    self.wearcardview.close()
                if temp == 5:
                    self.newcardview.close()
                self.wearlistview.close()
                self.machineview.close()
                self.hide()
                self.loginshow()
            return -2

    def wearCardShow(self, wearCardID):
        self.showGrid.addWidget(self.wearcardview)
        self.wearcardview.show()
        self.wearlistview.hide()
        self.curView = 4
        self.setWindowTitle("织轴卡详情")
        ret = self.getWearCardData(wearCardID=wearCardID)
        if ret == 0:
            self.wearCard()

    def wearCard(self):
        # print(self.wearCardData)
        self.wearcardview.wearCard.setItem(0, 1, QTableWidgetItem(self.wearCardData["machineName"]))
        self.wearcardview.wearCard.setItem(1, 1, QTableWidgetItem(self.wearCardData["serialNumber"]))
        self.wearcardview.wearCard.setItem(2, 1, QTableWidgetItem(self.wearCardData["plantName"]))
        self.wearcardview.wearCard.setItem(3, 1, QTableWidgetItem(self.wearCardData["machineModelName"]))
        self.wearcardview.wearCard.setItem(4, 1, QTableWidgetItem(str(self.wearCardData["yarnCount"])))
        self.wearcardview.wearCard.setItem(5, 1, QTableWidgetItem(str(self.wearCardData["shaftNo"])))
        self.wearcardview.wearCard.setItem(6, 1, QTableWidgetItem(self.wearCardData["shift"]))
        self.wearcardview.wearCard.setItem(7, 1, QTableWidgetItem(self.wearCardData["staff"]))
        self.wearcardview.wearCard.setItem(8, 1, QTableWidgetItem(self.wearCardData["monitor"]))
        self.wearcardview.wearCard.setItem(9, 1, QTableWidgetItem(str(self.wearCardData["quantity"])))
        self.wearcardview.wearCard.setItem(10, 1, QTableWidgetItem(str(self.wearCardData["totalLength"])))
        self.wearcardview.wearCard.setItem(11, 1, QTableWidgetItem(self.wearCardData["totalLengthDetail"]))
        self.wearcardview.wearCard.setItem(12, 1, QTableWidgetItem(self.wearCardData["variety"]))
        timestamp = int(self.wearCardData["gmtDoff"])
        timearray = time.localtime(timestamp / 1000)
        gmtDoff = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
        self.wearcardview.wearCard.setItem(13, 1, QTableWidgetItem(str(gmtDoff)))

    def onTriggeredRefreshAct_c(self):
        ret = self.getWearCardData(self.wearcardview.wearCardID)
        if ret == 0:
            self.wearCard()

    def getWearCardImage(self, table):
        painter = QPainter(table)
        painter.setPen(QPen(QBrush(Qt.black), 5, Qt.SolidLine))  # 设置颜色、线条粗细、实线
        painter.setRenderHint(QPainter.Antialiasing, True)  # 设置反锯齿
        font = painter.font()
        font.setPixelSize(12)  # 设置字体大小
        font.setBold(True)  # 设置粗体
        painter.setFont(font)
        pointArray = [QPoint(145, 46), QPoint(145, 70), QPoint(145, 94), QPoint(145, 119), QPoint(145, 143),
                      QPoint(145, 167), QPoint(145, 192), QPoint(145, 217), QPoint(145, 242), QPoint(145, 265),
                      QPoint(145, 291), QPoint(145, 315), QPoint(145, 340), QPoint(145, 364)]
        painter.drawText(pointArray[0], self.wearCardData["machineName"])
        painter.drawText(pointArray[1], self.wearCardData["serialNumber"])
        painter.drawText(pointArray[2], self.wearCardData["plantName"])
        painter.drawText(pointArray[3], self.wearCardData["machineModelName"])
        painter.drawText(pointArray[4], str(self.wearCardData["yarnCount"]))
        painter.drawText(pointArray[5], str(self.wearCardData["shaftNo"]))
        painter.drawText(pointArray[6], self.wearCardData["shift"])
        painter.drawText(pointArray[7], self.wearCardData["staff"])
        painter.drawText(pointArray[8], self.wearCardData["monitor"])
        painter.drawText(pointArray[9], str(self.wearCardData["quantity"]))
        painter.drawText(pointArray[10], str(self.wearCardData["totalLength"]))
        painter.drawText(pointArray[11], self.wearCardData["totalLengthDetail"])
        painter.drawText(pointArray[12], self.wearCardData["variety"])
        timestamp = int(self.wearCardData["gmtDoff"])
        timearray = time.localtime(timestamp / 1000)
        gmtDoff = str(time.strftime("%Y-%m-%d %H:%M:%S", timearray))
        name = str(time.strftime("%Y%m%d%H%M%S", timearray))
        painter.drawText(pointArray[13], gmtDoff)
        self.getRCode(painter)
        # rcode = QImage()
        # rcode.load("./images/" + str(self.wearcardview.wearCardID) + ".png")
        # painter.drawImage(QPoint(150, 382), rcode)
        painter.end()
        imageDir = r"./images/"
        if os.path.exists(imageDir) == False:
            os.mkdir(imageDir)
        self.fileName = imageDir + name + r".png"
        table.save(self.fileName)

    def onTriggeredPrintAct_c(self):
        with open("table2.png", "wb") as tablePng:
            tablePng.write(base64.b64decode(table2_png))
        tableImage = QImage()
        tableImage.load("table2.png")
        os.remove("table2.png")
        self.getWearCardImage(tableImage)
        preview = QPrintPreviewDialog(self.printer, self)
        preview.paintRequested.connect(self.plotPic)
        preview.exec()  # /* 等待预览界面退出 */

    def plotPic(self):
        painter = QPainter(self.printer)
        image = QImage()
        image.load(self.fileName)
        rect = painter.viewport()
        size = image.size()
        size.scale(rect.size(), Qt.KeepAspectRatio)  # //此处保证图片显示完整
        painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
        painter.setWindow(image.rect())
        painter.drawPixmap(0, 0, QPixmap.fromImage(image))

    def onTriggeredBackAct_c(self):
        self.wearlistview.show()
        self.wearcardview.close()
        self.setWindowTitle("织轴卡列表")
        self.curView = 3

    def newCardShow(self):
        self.showGrid.addWidget(self.newcardview)
        self.newcardview.show()
        self.wearlistview.hide()
        self.curView = 5
        self.setWindowTitle("织轴卡详情(最新)")
        ret = self.jsj.weaverCardList(pageNo=1, pageSize=self.maxPageSize, machineId=self.machineId)
        if ret == 0:
            data = self.jsj.wearListData
            self.wearListData = data["data"]
            wearCardID = self.wearListData["rows"][0]["id"]
        elif ret == -1:
            QMessageBox.warning(self, "提示", self.jsj.message + "\n由于网络原因导致账号离线，请重启软件并登陆", QMessageBox.Ok,
                                QMessageBox.Ok)
            return
        else:
            self.curView = 0
            if QMessageBox.warning(self, "提示", "数据获取失败，请检查网络是否可用!    ",
                                   QMessageBox.Ok, QMessageBox.Ok) == QMessageBox.Ok:
                self.newcardview.close()
                self.wearlistview.close()
                self.machineview.close()
                self.hide()
                self.loginshow()
                return
        print("=======OK========")
        ret = self.getWearCardData(wearCardID=wearCardID)
        if ret == 0:
            self.newCard()

    def newCard(self):
        # print(self.wearCardData)
        self.newcardview.wearCard.setItem(0, 1, QTableWidgetItem(self.wearCardData["machineName"]))
        self.newcardview.wearCard.setItem(1, 1, QTableWidgetItem(self.wearCardData["serialNumber"]))
        self.newcardview.wearCard.setItem(2, 1, QTableWidgetItem(self.wearCardData["plantName"]))
        self.newcardview.wearCard.setItem(3, 1, QTableWidgetItem(self.wearCardData["machineModelName"]))
        self.newcardview.wearCard.setItem(4, 1, QTableWidgetItem(str(self.wearCardData["yarnCount"])))
        self.newcardview.wearCard.setItem(5, 1, QTableWidgetItem(str(self.wearCardData["shaftNo"])))
        self.newcardview.wearCard.setItem(6, 1, QTableWidgetItem(self.wearCardData["shift"]))
        self.newcardview.wearCard.setItem(7, 1, QTableWidgetItem(self.wearCardData["staff"]))
        self.newcardview.wearCard.setItem(8, 1, QTableWidgetItem(self.wearCardData["monitor"]))
        self.newcardview.wearCard.setItem(9, 1, QTableWidgetItem(str(self.wearCardData["quantity"])))
        self.newcardview.wearCard.setItem(10, 1, QTableWidgetItem(str(self.wearCardData["totalLength"])))
        self.newcardview.wearCard.setItem(11, 1, QTableWidgetItem(self.wearCardData["totalLengthDetail"]))
        self.newcardview.wearCard.setItem(12, 1, QTableWidgetItem(self.wearCardData["variety"]))
        timestamp = int(self.wearCardData["gmtDoff"])
        timearray = time.localtime(timestamp / 1000)
        gmtDoff = time.strftime("%Y-%m-%d %H:%M:%S", timearray)
        self.newcardview.wearCard.setItem(13, 1, QTableWidgetItem(str(gmtDoff)))

    def onTriggeredRefreshAct_n(self):
        ret = self.jsj.weaverCardList(pageNo=1, pageSize=self.maxPageSize, machineId=self.machineId)
        if ret == 0:
            data = self.jsj.wearListData
            self.wearListData = data["data"]
            wearCardID = self.wearListData["rows"][0]["id"]
        elif ret == -1:
            QMessageBox.warning(self, "提示", self.jsj.message + "\n由于网络原因导致账号离线，请重启软件并登陆", QMessageBox.Ok,
                                QMessageBox.Ok)
            return
        else:
            self.curView = 0
            if QMessageBox.warning(self, "提示", "数据获取失败，请检查网络是否可用!    ",
                                   QMessageBox.Ok, QMessageBox.Ok) == QMessageBox.Ok:
                self.newcardview.close()
                self.wearlistview.close()
                self.machineview.close()
                self.hide()
                self.loginshow()
                return
        ret = self.getWearCardData(wearCardID=wearCardID)
        if ret == 0:
            self.newCard()

    def onTriggeredPrintAct_n(self):
        self.onTriggeredPrintAct_c()

    def onTriggeredBackAct_n(self):
        self.wearlistview.show()
        self.newcardview.close()
        self.setWindowTitle("织轴卡列表")
        self.curView = 3

    def getRCode(self, painter):
        """
        获得二维码，并将二维码加载到织轴卡中
        :param painter:
        :return:
        """
        # 初步生成二维码图像
        qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=3, border=1)
        url = "http://www.tssmax.cn/htzg/weaverdetail.html?id=" + str(self.wearcardview.wearCardID)
        qr.add_data(url)
        qr.make(fit=True)

        # 获得Image实例并把颜色模式转换为RGBA
        img = qr.make_image()
        img = img.convert("RGBA")

        # 打开logo文件
        logo = Image.open("logo.png")

        # 计算logo的尺寸
        img_w, img_h = img.size
        print(img_w, img_h)
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        # 比较并重新设置logo文件的尺寸
        log_w, log_h = logo.size
        print(log_w, log_h)
        if log_w > size_w:
            log_w = size_w
        if log_h > size_h:
            log_h = size_h
        icon = logo.resize((log_w, log_h), Image.ANTIALIAS)

        # 计算logo的位置，并复制到二维码图像中
        w = int((img_w - log_w) / 2)
        h = int((img_h - log_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon, (w, h), icon)
        img.save(str(self.wearcardview.wearCardID) + ".png")

        # 将二维码加载到织轴卡中
        qrcodeImg = QImage()
        qrcodeImg.load(str(self.wearcardview.wearCardID) + ".png")
        os.remove(str(self.wearcardview.wearCardID) + ".png")
        point = QPoint(int((380 - img_w) / 2) + 10, int((150 - img_h) / 2) + 370)
        painter.drawImage(point, qrcodeImg)


def main():
    jslf = jsjshow.jsj()
    app = QtWidgets.QApplication(sys.argv)
    mainwin = mainView(jslf)
    # mainwin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    pass
