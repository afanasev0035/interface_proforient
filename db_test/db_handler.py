import sqlite3

class str_db(object):
    def init_v1(self, text, index):
        index = index + 1
        self.quest = "NULL"
        self.answer1 = "NULL"
        self.answer2 = "NULL"
        self.name = text
        self.count = 0
        self.index = index
        
        con = sqlite3.connect('db_test/db.db')
        cur = con.cursor()

        cur.execute("SELECT question FROM '%s' WHERE id = '%d'" % (text, index))
        self.quest = cur.fetchall()[0][0]

        cur.execute("SELECT answer1 FROM '%s' WHERE id = '%d'" % (text, index))
        self.answer1 = cur.fetchall()[0][0]

        cur.execute("SELECT answer2 FROM '%s' WHERE id = '%d'" % (text, index))
        self.answer2 = cur.fetchall()[0][0]

        cur.execute("SELECT COUNT(*) as count FROM '%s'" % text)
        self.count = cur.fetchall()[0][0]

        cur.close()
        con.close()
    
    def init_v2(self, text, index):
        index = index + 1
        self.quest = "NULL"
        self.name = text
        self.count = 0
        self.index = index
        
        con = sqlite3.connect('db_test/db.db')
        cur = con.cursor()

        cur.execute("SELECT question FROM '%s' WHERE id = '%d'" % (text, index))
        self.quest = cur.fetchall()[0][0]

        cur.execute("SELECT COUNT(*) as count FROM '%s'" % text)
        self.count = cur.fetchall()[0][0]

        cur.close()
        con.close()

    def init_v3(self, text):
        con = sqlite3.connect('db_test/db.db')
        cur = con.cursor()

        cur.execute("SELECT conclusion FROM Выводы")
        self.concl = cur.fetchall()[0][0]

        cur.close()
        con.close()

def input_answer(text, index, answer):
        
    con = sqlite3.connect('db_test/db.db')
    cur = con.cursor()
    if (answer):
        cur.execute("UPDATE '%s' SET check1=1, check2=0 WHERE id = '%d'" % (text, index))
    else:
        cur.execute("UPDATE '%s' SET check1=0, check2=1 WHERE id = '%d'" % (text, index))

    con.commit()
    cur.close()
    con.close()

def input_text(text, index, answer):
        
    con = sqlite3.connect('db_test/db.db')
    cur = con.cursor()
    cur.execute("UPDATE '%s' SET answer = '%s' WHERE id = '%d'" % (text, answer, index))
    con.commit()
    cur.close()
    con.close()

def count_record(text):
    con = sqlite3.connect('db_test/db.db')
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) as count FROM '%s'" % text)
    return cur.fetchall()[0][0]
