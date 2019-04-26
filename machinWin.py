# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'machinWin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(630, 520)
        self.machineTable = QtWidgets.QTableWidget(Form)
        self.machineTable.setGeometry(QtCore.QRect(0, 35, 630, 480))
        self.machineTable.setMidLineWidth(0)
        self.machineTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.machineTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.machineTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.machineTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.machineTable.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.machineTable.setRowCount(15)
        self.machineTable.setColumnCount(4)
        self.machineTable.setObjectName("machineTable")
        self.machineTable.horizontalHeader().setSortIndicatorShown(False)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "machines"))

