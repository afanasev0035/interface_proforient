from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_test import *

class Ui_Writen_test(object):
    def setupUi(self, Writen_test, text, index):
        Writen_test.setObjectName(text)
        Writen_test.resize(910, 349)
        self.centralwidget = QtWidgets.QWidget(Writen_test)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 37, 800, 121))
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
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 220, 800, 30))
        self.lineEdit.setObjectName("textEdit")
        Writen_test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Writen_test, text, index)
        QtCore.QMetaObject.connectSlotsByName(Writen_test)

    def retranslateUi(self, Writen_test, text, index):
        _translate = QtCore.QCoreApplication.translate
        db = str_db()
        db.init(text, index)
        Writen_test.setWindowTitle(_translate("Test", text))
        self.label.setText(_translate("Test", db.quest))
        self.pushButton.setText(_translate("Writen_test", "Вперед"))
        self.pushButton_2.setText(_translate("Writen_test", "Вернуться"))
        self.lineEdit.setPlaceholderText(_translate("Writen_test", "Введите текст"))
    
    def record_db(self, index, text):
        if (self.lineEdit.text() != ""):
            print(self.lineEdit.text())
            return 0
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Введите ответ")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            return (-1)
