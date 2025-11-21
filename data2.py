import sqlite3
class database :
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS citizens (id PRIMARY KEY ,fname TEXT , lname TEXT , address TEXT , phone INTEGER)")
        self.con.commit()
    def insert_rec(self,fname,lname,address,phone):
        self.cur.execute("INSERT INTO citizens (id,fname,lname,score) values (NULL,?,?,?)",(fname,lname,address,phone))
        self.con.commit()
    def select(self):
        self.cur.execute('SELECT * FROM citizens')
        return self.cur.fetchall()
        
db1 = database("F:/mydtabase1.db")