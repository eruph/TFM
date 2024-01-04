from base_operator import BaseOperator

class TagOperator(BaseOperator):
    def __init__(self):
        super().__init__()
        self.commands = {
            "new":lambda args: self.crifp(args,1,self.create_new_tag),
            "lst":lambda args: self.crifp(args,0,self.show_existing_tags)
        }

    def create_new_tag(self, tag:str) -> None:
        '''new example: new tag_name'''
        if self.db.does_table_exist(tag):
            print("{} tag is already created!")
            return None

        self.db.create_tag(tag)

    def show_existing_tags(self) -> None:
        '''lst example: lst'''
        for tag in self.db.get_tags():
            print(tag)
