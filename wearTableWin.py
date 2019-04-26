# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wearTableWin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 520)
        self.wearTable = QtWidgets.QTableWidget(Form)
        self.wearTable.setGeometry(QtCore.QRect(0, 35, 630, 480))
        self.wearTable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wearTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wearTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.wearTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.wearTable.setAlternatingRowColors(False)
        self.wearTable.setRowCount(15)
        self.wearTable.setColumnCount(4)
        self.wearTable.setObjectName("wearTable")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

