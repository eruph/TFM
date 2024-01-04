from base_operator import BaseOperator
import os
from typing import Callable, Any

class Operator(BaseOperator):
    '''class that provides interface to all operation that can be apllied to files/tagsx'''
    def __init__(self):
        super().__init__()
        self.commands = {
            "scan": lambda args: self.crifp(args,1,self.scan),
            "list": lambda args: self.crifp(args,1,self.list_table_content)
        }
        
    #check and run if possible:for short 
    def crifp(self,args:list, required_args_amount:int, fn:Callable[..., Any]) -> bool:
        '''if len of passed arguments is equal to required one, then call function. otherwise print doc for the function'''
        if len(args) != required_args_amount:
            print(fn.__doc__)
        else:
            fn(*args)
    
    def scan(self,root: str) -> None:
        '''scan example: scan root_directory'''
        #this functions scans passed directory and adds all its content to tagless table
        
        if not os.path.exists(root):
            print("{} doesn't exist!".format(root))
            return None

        next_id = self.db.get_tagless_max()

        print_progress = lambda top, item: print("{}/{} is staged as tagless!".format(top,item))
        for top, dirs, files in os.walk(root):
            for dir in dirs:
                self.db.add_tagless_item(next_id,top,dir)
                next_id += 1
                print_progress(top,dir)
                
            for file in files:
                self.db.add_tagless_item(next_id,top,file)
                next_id += 1
                print_progress(top,file)


    def list_table_content(self, table:str) -> None:
        '''list example: list table_name'''

        #TODO: do better output
        prnt = lambda left, right: print("{} {} {}".format(left," "*10,right))
        if self.db.does_table_exist(table):
            prnt(":path:",":name:")
            for path, name in self.db.get_table_content(table):
                prnt(path,name)
        else:
            print("'{}' table doesn't exist!".format(table))
        
