from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QAction, QMainWindow
from db_test import *


class Ui_auth_window(object):
    def setupUi(self, auth_window):
        auth_window.setObjectName("auth_window")
        auth_window.resize(231, 111)
        auth_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(auth_window)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 211, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.lineEdit_lastname = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_lastname.setObjectName("lineEdit_lastname")
        self.verticalLayout.addWidget(self.lineEdit_lastname)
        self.pushButton_enter = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.verticalLayout.addWidget(self.pushButton_enter)
        auth_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(auth_window)
        QtCore.QMetaObject.connectSlotsByName(auth_window)
        quit = QAction("Quit", auth_window)
        quit.triggered.connect(auth_window.closeEvent)

    def retranslateUi(self, auth_window):
        _translate = QtCore.QCoreApplication.translate
        auth_window.setWindowTitle(_translate("auth_window", "Окно авторизации"))
        self.lineEdit_name.setPlaceholderText(_translate("auth_window", " Имя"))
        self.lineEdit_lastname.setPlaceholderText(_translate("auth_window", " Фамилия"))
        self.pushButton_enter.setText(_translate("auth_window", "Войти"))

    
    def closeEvent(self, event):
        print("X is clicked")

def check_user(self):
    if (self.lineEdit_lastname.text() != "" and self.lineEdit_name.text() != ""):
        user_id = check_user_in_db(self.lineEdit_name.text(), self.lineEdit_lastname.text())
        return user_id
    else:
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Заполните поля")
        error.setIcon(QMessageBox.Warning)
        error.setStandardButtons(QMessageBox.Ok)
        error.exec_()
        return (-1)

