import sqlite3
from format import *
path_db = "db_test/db.db"

#### Новый код

#### Получение user_id

def check_user_in_db(name, last_name):
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute("SELECT user_id FROM persons WHERE name = '%s' AND last_name = '%s'" % (name, last_name))
    user_id = cur.fetchall()
    if user_id == []:
        user_id = cur.execute("SELECT max(user_id) FROM persons").fetchall()[0][0]
        if user_id != None and user_id != "":
            user_id = user_id + 1
        else:
            user_id = 1
        data = (user_id, name, last_name)
        cur.execute("INSERT INTO persons (user_id, name, last_name) VALUES(?, ?, ?)", data)
        con.commit()
    else:
        user_id = user_id[0][0]
    cur.close()
    con.close()
    return user_id

 

#### Получение вопроса

def get_question_from_db(test):
    con = sqlite3.connect(path_db)
    cur = con.cursor()

    cur.execute("SELECT name_quest FROM test WHERE test_name = '%s' AND quest_id = '%d'" % (test.test_name, test.quest_id))
    value = cur.fetchall()
    if value != []:
        value = value[0][0]
    else:
        return 1
    if value != None and value != "":
        test.name_quest = value
    else:
        cur.close()
        con.close()
        return 1
    
    cur.execute("SELECT answer_n1 FROM test WHERE test_name = '%s' AND quest_id = '%d'" % (test.test_name, test.quest_id))
    value = cur.fetchall()[0][0]
    if value != None and value != "":
        test.answer_n1 = value
    else:
        cur.close()
        con.close()
        return 2

    cur.execute("SELECT answer_n2 FROM test WHERE test_name = '%s' AND quest_id = '%d'" % (test.test_name, test.quest_id))
    value = cur.fetchall()[0][0]
    if value != None and value != "":
        test.answer_n2 = value
    else:
        cur.close()
        con.close()
        return 3

    cur.execute("SELECT answer_n3 FROM test WHERE test_name = '%s' AND quest_id = '%d'" % (test.test_name, test.quest_id))
    value = cur.fetchall()[0][0]
    if value != None and value != "":
        test.answer_n3 = value
    else:
        cur.close()
        con.close()
        return 4

    cur.execute("SELECT answer_n4 FROM test WHERE test_name = '%s' AND quest_id = '%d'" % (test.test_name, test.quest_id))
    value = cur.fetchall()[0][0]
    if value != None and value != "":
        test.answer_n4 = value
    else:
        cur.close()
        con.close()
        return 5

    cur.close()
    con.close()
    return 6

def get_count_question_test(test_name):
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM test WHERE test_name = '%s'" % (test_name))
    value = cur.fetchall()
    if value != []:
        value = value[0][0]
    else:
        value = 0
    cur.close()
    con.close()
    return value

def check_repeat_test_id(user_id, test_name):
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute("SELECT test_id FROM user WHERE user_id = '%s'" % (user_id))
    test_id = cur.fetchall()
    for i in test_id:
        name = cur.execute("SELECT test_name FROM test_users WHERE test_id = '%s'" % (i[0]))
        name = name.fetchall()
        if name != []:
            name = name[0][0]
            if name == test_name:
                cur.close()
                con.close()
                return i[0]
    cur.close()
    con.close()
    return -1

def check_test_result(user_id, test_name, count):
    check = 0
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute("SELECT test_id FROM user WHERE user_id = '%s'" % (user_id))
    test_id = cur.fetchall()
    for i in test_id:
        name = cur.execute("SELECT test_name FROM test_users WHERE test_id = '%s'" % (i[0]))
        name = name.fetchall()
        if name != []:
            name = name[0][0]
            for j in test_name:
                if name == j:
                    check = check + 1
                    break
    cur.close()
    con.close()
    if check != count:
        return -1
    else:
        return check

def init_test_id(user_id, test_name, quest):

    quest.back_test_id = check_repeat_test_id(user_id, test_name)   
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute("SELECT max(test_id) FROM test_users")
    test_id = cur.fetchall()
    if test_id == []:
        test_id = 1
    else:
        test_id = test_id[0][0]
        if test_id != None and test_id != "":
            test_id = test_id + 1
        else:
            test_id = 1
    data = (user_id, test_id)
    cur.execute("INSERT INTO user (user_id, test_id) VALUES (?, ?)", data)
    data1 = (test_id, test_name)
    cur.execute("INSERT INTO test_users (test_id, test_name) VALUES(?, ?)", data1)
    con.commit()
    cur.close()
    con.close()
    return test_id

def record_in_db(num, quest, test_id):
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    quest_id = quest.quest_id - 1
    test_id = quest.test_id
    data = (test_id, num, quest_id)
    cur.execute("SELECT user_response FROM user_response WHERE test_id = '%d' AND user_response_id = '%d'" % (test_id, quest_id))
    value = cur.fetchall()
    if value == []:
        cur.execute("INSERT INTO user_response (test_id, user_response, user_response_id) VALUES(?, ?, ?)", data)
    else:
        cur.execute("UPDATE  user_response SET  user_response = '%s' WHERE test_id = '%s' AND user_response_id = '%d'" % (num, test_id, quest_id))
    con.commit()
    cur.close()
    con.close()
    return

def delete_record_db(quest):
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    cur.execute("DELETE FROM user_response WHERE test_id = '%s'" % quest.test_id)
    cur.execute("DELETE FROM test_users WHERE test_id = '%s'" % quest.test_id)
    cur.execute("DELETE FROM user WHERE test_id = '%s'" % quest.test_id)
    con.commit()
    cur.close()
    con.close()
    return

def get_conclusion(name_button, user_id):
    con = sqlite3.connect(path_db)
    cur = con.cursor()
    if (name_button == "Блок интелекта"):
        cur.execute("SELECT conclusion_1 FROM conclusion WHERE user_id = '%d'" % user_id)
    elif (name_button == "Блок профориент."):
        cur.execute("SELECT conclusion_2 FROM conclusion WHERE user_id = '%d'" % user_id)
    elif (name_button == "Блок личности"):
        cur.execute("SELECT conclusion_3 FROM conclusion WHERE user_id = '%d'" % user_id)
    else:
        cur.execute("SELECT conclusion FROM conclusion WHERE user_id = '%d'" % user_id)
    name = cur.fetchall()
    if name == []:
        name = "Ошибка чтения из БД"
    else:
        name = name[0][0]
    cur.close()
    con.close()
    return name
