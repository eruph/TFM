from DBManager import *
from typing import Callable, Any

#there should be only one instance of data base manager
class BaseOperator:
    def __init__(self):
        self.db = DBManager()

    #check and run if possible:for short 
    def crifp(self,args:list, required_args_amount:int, fn:Callable[..., Any]) -> bool:
        '''if len of passed arguments is equal to required one, then call function. otherwise print doc for the function'''
        if len(args) != required_args_amount:
            print(fn.__doc__)
        else:
            fn(*args)
