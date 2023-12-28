import sqlite3 as sql
import os


class DBManager:
    def __init__(self):
        self.is_first_start = os.path.exists("tfm.db")
        self.connection = sqlite3.connect('tfm.db')
        self.cursor = connection.cursor()

        if self.is_first_start: self.__create_special_tables()
    def __del__(self):
        self.connection.close()

    def __create_special_tables(self):
        pass

    
