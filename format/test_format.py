from typing import Counter, Text
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from db_test import *
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QAction


class question(object):
    def init(self, test_name, Mainindow):
        self.test_name = test_name
        self.quest_id = 1
        self.name_quest = "NULL"
        self.answer_n1 = "NULL"
        self.answer_n2 = "NULL"
        self.answer_n3 = "NULL"
        self.answer_n4 = "NULL"
        self.status = 0
        self.test_id = -1
        self.back_test_id = -1
        self.count = get_count_question_test(test_name) #получение кол-ва вопросов в тесте
    
    def get_question(self):
            self.status = get_question_from_db(self)
            self.quest_id = self.quest_id + 1

    def check_num(self):
        if self.quest_id <= self.count:
            return 0
        else:
            return -1
    
    def first_test(self):
        if self.quest_id < 1:
            return 0
        else:
            return -1


class Ui_Test(object):

    def setupUi(self, Test, quest):
        Test.setObjectName("Test")
        Test.resize(836, 323)
        self.centralwidget = QtWidgets.QWidget(Test)
        self.centralwidget.setObjectName("centralwidget")
        self.label_quest = QtWidgets.QLabel(self.centralwidget)
        self.label_quest.setGeometry(QtCore.QRect(20, 37, 800, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_quest.sizePolicy().hasHeightForWidth())
        self.label_quest.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_quest.setFont(font)
        self.label_quest.setStyleSheet("background-color: rgb(255, 253, 238);")
        self.label_quest.setText("")
        self.label_quest.setObjectName("label_quest")
        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(730, 270, 88, 34))
        self.pushButton_next.setObjectName("pushButton_next")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(630, 270, 88, 34))
        self.pushButton_back.setObjectName("pushButton_back")
        self.quest = quest
        if quest.status > 2:
            self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_1.setGeometry(QtCore.QRect(20, 150, 800, 22))
            self.radioButton_1.setText("")
            self.radioButton_1.setObjectName("radioButton_1")
        if quest.status > 3:
            self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_2.setGeometry(QtCore.QRect(20, 180, 800, 22))
            self.radioButton_2.setText("")
            self.radioButton_2.setObjectName("radioButton_2")
        if quest.status > 4:
            self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_3.setGeometry(QtCore.QRect(20, 210, 800, 22))
            self.radioButton_3.setText("")
            self.radioButton_3.setObjectName("radioButton_3")
        if quest.status > 5:
            self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
            self.radioButton_4.setGeometry(QtCore.QRect(20, 240, 800, 22))
            self.radioButton_4.setText("")
            self.radioButton_4.setObjectName("radioButton_4")
        if quest.status == 2:
            self.lineEdit_answer = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit_answer.setGeometry(QtCore.QRect(20, 222, 801, 31))
            self.lineEdit_answer.setObjectName("lineEdit_answer")

        Test.setCentralWidget(self.centralwidget)
        QtCore.QEvent
        self.retranslateUi(Test, quest)
        QtCore.QMetaObject.connectSlotsByName(Test)
    def retranslateUi(self, Test, quest):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test",  quest.test_name))
        self.pushButton_next.setText(_translate("Test", "Вперед"))
        self.pushButton_back.setText(_translate("Test", "Вернуться"))
        self.label_quest.setText(_translate("Test","  " + quest.name_quest))
        if quest.status == 2:
            self.lineEdit_answer.setPlaceholderText(_translate("Test", "  Введите ответ"))
        if quest.status > 2:
            self.radioButton_1.setText(_translate("Test", quest.answer_n1))
        if quest.status > 3:
            self.radioButton_2.setText(_translate("Test", quest.answer_n2))
        if quest.status > 4:
            self.radioButton_3.setText(_translate("Test", quest.answer_n3))
        if quest.status > 5:
            self.radioButton_3.setText(_translate("Test", quest.answer_n4))

    def check_radiobutton(self, quest):
        if quest.status > 2:
            if self.radioButton_1.isChecked():
                return 1
        if quest.status > 3:
            if self.radioButton_2.isChecked():
                return 2
        if quest.status > 4:
            if self.radioButton_3.isChecked():
                return 3
        if quest.status > 5:
            if self.radioButton_4.isChecked():
                return 4
        return 0

    def record_db(self, quest, user_id):
        if quest.status == 2:
            if (self.lineEdit_answer.text() != ""):
                record_in_db(self.lineEdit_answer.text(), quest, user_id)
                return 0
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Введите ответ")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                return (-1)
        else:
            num = self.check_radiobutton(quest)
            if num != 0:
                record_in_db(num, quest, user_id)
                return 0
            else:
                error = QMessageBox()
                error.setWindowTitle("Ошибка")
                error.setText("Выберите ответ")
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                return (-1)



    def closeEvent(self):
        delete_record_db(self.quest)
