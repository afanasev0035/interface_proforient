from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from test_vybor_otveta import *
from main_int import *
from check_db import *
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


def open_test(text):

    if (check_window(text) == 0):
        return

    global Test 
    Test = QtWidgets.QMainWindow()
    ui_2 = Ui_Test()
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
    
    def record_db(ui, index, text):
        if (ui_2.checkBox.isChecked() or ui_2.checkBox_2.isChecked()):
            if ui_2.checkBox.isChecked():
                input_answer(text, index, True)    
            else:
                input_answer(text, index, False)
            open_test(text)
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Выберите вариант ответа")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
        error.exec_()



    ui_2.pushButton_2.clicked.connect(returnToMain)
    ui_2.pushButton.clicked.connect(lambda: record_db(ui_2, Tests[0], text))

ui.pushButton.clicked.connect(lambda: open_test(ui.pushButton.text()))

sys.exit(app.exec_())