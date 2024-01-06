import sqlite3 as sql
import os


class DBManager:
    def __init__(self):
        self.is_first_start = not os.path.exists("tfm.db")
        self.connection = sql.connect('tfm.db')
        self.cursor = self.connection.cursor()
        
        if self.is_first_start: self.__create_special_tables()

        #load script to create table
        with open("sql/create_tag_table.sql","r") as f:
            self.tag_table_req = f.read()
            
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
        print("tfm.db has been created!")

    def _get_table_max(self, table:str) -> int:
        '''common function to retrieve size of table'''
        self.cursor.execute("SELECT MAX(id) FROM {}".format(table))
        result = self.cursor.fetchall()
        if result[0][0] is None:
            return 0
        else:
            return result[0][0]

    def get_tagless_max(self) -> int: return self._get_table_max("tagless")

    def add_tagless_item(self,id:int,path:str,name:str) -> None:
        self.cursor.execute("INSERT INTO tagless (id, path, name) VALUES({}, '{}', '{}')".format(id,path,name))
        self.connection.commit()

    def does_table_exist(self, table:str) -> bool:
        #if there is no such table None is returned.
        self.cursor.execute("SELECT name FROM tags WHERE name = '{}'".format(table))
        result = self.cursor.fetchall()
        return len(result) > 0

    def get_table_content(self, table:str) -> list:
        '''returns list of pairs made up from strings'''
        self.cursor.execute("SELECT path, name FROM {}".format(table))
        return self.cursor.fetchall()


    def create_tag(self, tag:str) -> None:
        '''create new table associated with provided tag'''
        #Note: check tag existence before creation
        self.cursor.execute(self.tag_table_req.format(tag))
        self.connection.commit()

        #make a record there is such tag
        tags_size = self._get_table_max("tags")
        self.cursor.execute("INSERT INTO tags (id,name,parent) VALUES({},'{}','')".format(tags_size+1,tag))
        self.connection.commit()

    def get_tags(self) -> list:
        '''return list of strings, containg names of all existing tags'''
        self.cursor.execute("SELECT name from tags")
        result = self.cursor.fetchall()
        return [x[0] for x in result]
        

    
