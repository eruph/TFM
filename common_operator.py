from base_operator import BaseOperator
import os
from tag_operator import TagOperator

class Operator(BaseOperator):
    '''class that provides interface to all operation that can be apllied to files/tags'''
    def __init__(self):
        super().__init__()
        self.commands = {
            "scan": lambda args: self.crifp(args,1,self.scan),
            "list": lambda args: self.crifp(args,1,self.list_table_content)
        }

        #add tag operations
        self.tag_ops = TagOperator().commands
        for op in self.tag_ops.keys():
            self.commands[op] = self.tag_ops[op]
        
    
    def scan(self,root: str) -> None:
        '''scan example: scan root_directory'''
        #this functions scans passed directory and adds all its content to tagless table
        
        if not os.path.exists(root):
            print("{} doesn't exist!".format(root))
            return None

        next_id = self.db.get_tagless_max()+1 # add 1, since we get max value and this value is already used

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
        
