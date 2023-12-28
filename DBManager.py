import sqlite3 as sql
import os


class DBManager:
    def __init__(self):
        self.is_first_start = not os.path.exists("tfm.db")
        self.connection = sql.connect('tfm.db')
        self.cursor = self.connection.cursor()
        
        if self.is_first_start: self.__create_special_tables()
    def __del__(self):
        self.connection.close()

    def __create_special_tables(self):
        with open("sql/create_base_tables.sql","r") as f:
            #it's available to execute only one statement in one time
            #so i split file with two requests with -- and then execute
            #them sequencesly
            req1, req2 = f.read().split('--')
            self.cursor.execute(req1)
            self.cursor.execute(req2)
            self.connection.commit()
            self.connection.close()
        print("tfm.db has been created!")

    
