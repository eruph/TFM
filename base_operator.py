from DBManager import *

#there should be only one instance of data base manager
class BaseOperator:
    def __init__(self):
        self.db = DBManager()
