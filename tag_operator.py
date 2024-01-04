from base_operator import BaseOperator


class TagOperator(BaseOperator):
    def __init__(self):
        super().__init__()
        self.commands = {}
