from os import error, name
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow
from format import *
from db_test import *
import sys

from format.test_format import question

test_name_intell = ('Айзенк', 'Кеттел', 'Векслер')
test_name_prof = ('Дж. Голонда', 'Е. А. Климова', 'Г. В. Рязапкина')
test_name_lich = ('Томас-Килманн', 'Юнга', 'Бриггс-Майерс')
test_name_all = ('Айзенк', 'Кеттел', 'Векслер', 'Дж. Голонда', 'Е. А. Климова', 'Г. В. Рязапкина', 'Томас-Килманн', 'Юнга', 'Бриггс-Майерс')


app = QApplication(sys.argv)
Authindow = QMainWindow()
ui = Ui_auth_window()
ui.setupUi(Authindow)
Authindow.show()
global user_id


def check_user_id(auth):
    user_id = check_user(auth)
    if user_id == -1:
        return
    else:
        open_win(user_id)

def open_win(user_id):   
    global Mainindow
    Mainindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Mainindow)
    Authindow.close()
    Mainindow.show()

    def init_test(name_test):
        quest = question()
        quest.init(name_test, Mainindow)
        quest.test_id = init_test_id(user_id, name_test, quest)
        Mainindow.close()
        create_test(quest)
        

    def next_test(quest, Test, ui):
        if ui.record_db(quest, user_id) != 0:
            return

        if quest.check_num() != 0:
            if quest.back_test_id != -1:
                quest.test_id =  quest.back_test_id
                delete_record_db(quest)
                Mainindow.show()
            Test.close()
        else:
            create_test(quest)
        
    def back_test(quest, Test):
        quest.quest_id = quest.quest_id - 2
        if quest.first_test() != 0:
            create_test(quest)
        else:
            delete_record_db(quest)
            Mainindow.show()
            Test.close()
            return
    
    def create_test(quest):
        quest.get_question()
        if quest.status == 1:
            return
        global Test 
        Test = QtWidgets.QMainWindow()
        ui = Ui_Test()
        ui.setupUi(Test, quest)
        app.aboutToQuit.connect(ui.closeEvent)
        Test.show()

        ui.pushButton_next.clicked.connect(lambda: next_test(quest, Test, ui))
        ui.pushButton_back.clicked.connect(lambda: back_test(quest, Test))
    
    def result(name_button, ui):

        if (name_button == "Блок интелекта"):
            test_name = test_name_intell
            count = 3 
        elif (name_button == "Блок профориент."):
            test_name = test_name_prof
            count = 3
        elif (name_button == "Блок личности"):
            test_name = test_name_lich
            count = 3
        else:
            test_name = test_name_all
            count = 6

        check = check_test_result(user_id, test_name, count)

        if check == -1:
            if count == 3:
                ui.err_msg()
            else:
                ui.err_msg_all()
        else:
            open_result(name_button)
    
    def open_result(name_button):
        global Test
        Test = QtWidgets.QMainWindow()
        ui_2 = Ui_Result()
        ui_2.setupUi(Test, name_button, user_id)
        Test.show()

        def returnToMain():
            Test.close()

        ui_2.pushButton.clicked.connect(returnToMain)


    # Активации кнопок тестов главного окна
    ui.pushButton_ayzenk.clicked.connect(lambda: init_test(ui.pushButton_ayzenk.text()))
    ui.pushButton_all_result.clicked.connect(lambda: result(ui.pushButton_all_result.text(), ui))
    ui.pushButton_block_lich.clicked.connect(lambda: result(ui.pushButton_block_lich.text(), ui))
    ui.pushButton_block_proforient.clicked.connect(lambda: result(ui.pushButton_block_proforient.text(), ui))
    ui.pushButton_block_intell.clicked.connect(lambda: result(ui.pushButton_block_intell.text(), ui))

    # Активации кнопок результатов главного окна


# Активации главного окна
ui.pushButton_enter.clicked.connect(lambda: check_user_id(ui))


sys.exit(app.exec_())