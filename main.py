from os import error
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from format import *
from db_test import *

import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
global Tests
Tests = [0]

def check_window(text):
    if (Tests[0] == 0):
        MainWindow.close()
        return 1
    elif (Tests[0] < count_record(text)):
        Tests[Tests[0]].close()
        return 1
    else:
        Tests[Tests[0]].close()
        Tests.clear()
        Tests.append(0)
        MainWindow.show()
        return 0

def select_win_type(text):
    if text == "Айзенк":
        return Ui_Writen_test()
    else:
        return Ui_Test()

def open_test(text):

    if (check_window(text) == 0):
        return

    global Test 
    Test = QtWidgets.QMainWindow()
    ui_2 = select_win_type(text)
    ui_2.setupUi(Test, text, Tests[0])
    Test.show()
    Tests.append(Test)
    Tests[0] = Tests[0] + 1
 
    def returnToMain():
        Tests.pop()
        Tests[0] = Tests[0] - 1
        Test.close()
        if (Tests[0] == 0):
            MainWindow.show()
        else:
            Tests[Tests[0]].show()
    
    def record(ui, index, text):
        if (0 == ui.record_db(index, text)):
            open_test(text)

    ui_2.pushButton_2.clicked.connect(returnToMain)
    ui_2.pushButton.clicked.connect(lambda: record(ui_2, Tests[0], text))
    ui_2.pushButton.clicked.connect(lambda: record(ui_2, Tests[0], text))

ui.pushButton.clicked.connect(lambda: open_test(ui.pushButton.text()))

sys.exit(app.exec_())