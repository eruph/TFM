from DBManager import *
import os
from typing import Callable, Any

class Operator:
    '''class that provides interface to all operation that can be apllied to files/tagsx'''
    def __init__(self):
        self.commands = {
            "scan": lambda args: self.crifp(args,1,self.scan)
        }
        self.__db = DBManager()
        
    #check and run if possible:for short 
    def crifp(self,args:list, required_args_amount:int, fn:Callable[..., Any]) -> bool:
        '''if len of passed arguments is equal to required one, then call function. otherwise print doc for the function'''
        if len(args) != required_args_amount:
            print(fn.__doc__)
        else:
            fn(*args)
    
    def scan(self,root: str):
        '''scan example: scan root_directory'''
        #this functions scans passed directory and adds all its content to tagless table
        
        if not os.path.exists(root):
            print("{} doesn't exist!".format(root))
            return None

        next_id = self.__db.get_tagless_max()

        print_progress = lambda top, item: print("{}/{} is staged as tagless!".format(top,item))
        for top, dirs, files in os.walk(root):
            for dir in dirs:
                self.__db.add_tagless_item(next_id,top,dir)
                next_id += 1
                print_progress(top,dir)
                
            for file in files:
                self.__db.add_tagless_item(next_id,top,file)
                next_id += 1
                print_progress(top,file)
        
