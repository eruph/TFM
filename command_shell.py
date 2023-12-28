import sys
import os


class CommandShell:
    def __init__(self):
        self.commands = {}
        
    def __run_interactively(self):
        while True:
            command = input(">>")
            if command not in self.commands.keys():
                print("command '{}' doesn't exist!".format(command))
            else:
                pass #extract args and run self.commands[command]
    def __run_cli(self):
        pass


    def run(self):
        if len(sys.argv) > 1:
            self.__run_cli()
        else:
            self.__run_interactively()
        
