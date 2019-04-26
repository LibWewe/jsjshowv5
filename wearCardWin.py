# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wearCardWin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 520)
        self.wearCard = QtWidgets.QTableWidget(Form)
        self.wearCard.setGeometry(QtCore.QRect(0, 35, 630, 480))
        self.wearCard.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wearCard.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wearCard.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.wearCard.setRowCount(14)
        self.wearCard.setColumnCount(2)
        self.wearCard.setObjectName("wearCard")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

