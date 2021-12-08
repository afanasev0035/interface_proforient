import sqlite3

class str_db(object):
    def init(self, text, index):
        index = index + 1
        self.quest = "NULL"
        self.answer1 = "NULL"
        self.answer2 = "NULL"
        self.name = text
        self.count = 0
        self.index = index
        
        con = sqlite3.connect(get_way_db(text))
        cur = con.cursor()

        cur.execute("SELECT question FROM ayzeka WHERE id = '%s'" % index)
        self.quest = cur.fetchall()[0][0]

        cur.execute("SELECT answer1 FROM ayzeka WHERE id = '%s'" % index)
        self.answer1 = cur.fetchall()[0][0]

        cur.execute("SELECT answer2 FROM ayzeka WHERE id = '%s'" % index)
        self.answer2 = cur.fetchall()[0][0]

        cur.execute("SELECT COUNT(*) as count FROM ayzeka")
        self.count = cur.fetchall()[0][0]

        cur.close()
        con.close()

def input_answer(text, index, answer):
        
    con = sqlite3.connect(get_way_db(text))
    cur = con.cursor()
    if (answer):
        cur.execute("UPDATE ayzeka SET check1=1, check2=0 WHERE id = '%s'" % index)
    else:
        cur.execute("UPDATE ayzeka SET check1=0, check2=1 WHERE id = '%s'" % index)

    con.commit()
    cur.close()
    con.close()

def count_record(text):
    con = sqlite3.connect(get_way_db(text))
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) as count FROM ayzeka")
    return cur.fetchall()[0][0]

def get_way_db(text):
    if text == "Айзенк":
        return "db_test/test_ayzek"
    else:
        return "db_test/test_ne_ayzek"