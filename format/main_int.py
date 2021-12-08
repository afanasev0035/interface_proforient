from PyQt5 import QtCore, QtGui, QtWidgets
from format.test_format import *
from db_test import *
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(552, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(193, 65, 166, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(24, 65, 136, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(416, 65, 88, 18))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(27, 95, 130, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(211, 95, 130, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(395, 95, 130, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(27, 145, 130, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(395, 145, 130, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(211, 145, 130, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(211, 195, 130, 40))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(395, 195, 130, 40))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(27, 195, 130, 40))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(171, 15, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(26, 300, 130, 40))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(394, 300, 130, 40))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 300, 130, 40))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(171, 250, 211, 27))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 350, 505, 40))
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система профориентации"))
        self.label.setText(_translate("MainWindow", "Профориентированность"))
        self.label_2.setText(_translate("MainWindow", "Структура интелекта"))
        self.label_3.setText(_translate("MainWindow", "Тип личности"))
        self.pushButton.setText(_translate("MainWindow", "Айзенк"))
        self.pushButton_2.setText(_translate("MainWindow", "Дж. Голонда"))
        self.pushButton_3.setText(_translate("MainWindow", "Томас-Килманн"))
        self.pushButton_4.setText(_translate("MainWindow", "Кеттелл"))
        self.pushButton_5.setText(_translate("MainWindow", "Юнга"))
        self.pushButton_6.setText(_translate("MainWindow", "Е. А. Климова"))
        self.pushButton_7.setText(_translate("MainWindow", "Г. В. Рязапкина "))
        self.pushButton_8.setText(_translate("MainWindow", "Бриггс-Майерс"))
        self.pushButton_9.setText(_translate("MainWindow", "Векслер"))
        self.label_4.setText(_translate("MainWindow", "Типы тестирования:"))
        self.pushButton_10.setText(_translate("MainWindow", "Блок интелекта"))
        self.pushButton_11.setText(_translate("MainWindow", "Блок личности"))
        self.pushButton_12.setText(_translate("MainWindow", "Блок профориент."))
        self.label_5.setText(_translate("MainWindow", "Результаты:"))
        self.pushButton_13.setText(_translate("MainWindow", "Обобщенный результат"))

   

