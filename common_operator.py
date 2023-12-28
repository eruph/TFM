from DBManager import *


class Operator:
    '''class that provides interface to all operation that can be apllied to files/tagsx'''
    def __init__(self):
        self.commands = {}
        self.__db = DBManager()
