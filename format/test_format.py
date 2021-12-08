from typing import Counter, Text
from PyQt5 import QtCore, QtGui, QtWidgets
from db_test import *

class Ui_Test(object):
    def setupUi(self, Test, text, index):
        Test.setObjectName(text)
        Test.resize(910, 349)
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 37, 800, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 253, 238);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 280, 88, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 280, 88, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 190, 105, 22))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 220, 105, 22))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        Test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test, text, index)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test, text, index):
        _translate = QtCore.QCoreApplication.translate
        db = str_db()
        db.init(text, index)
        Test.setWindowTitle(_translate("Test", text))
        self.label.setText(_translate("Test", db.quest))
        self.radioButton.setText(_translate("Test", db.answer1))
        self.radioButton_2.setText(_translate("Test", db.answer2))
        self.pushButton.setText(_translate("Test", "Вперед"))
        self.pushButton_2.setText(_translate("Test", "Вернуться"))
