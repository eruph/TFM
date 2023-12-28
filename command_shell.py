import sys
import os
from operator import *

class CommandShell:
    def __init__(self):
        #every command is repsented with lambda that takes list of argument(even if command doesn't require any additional data)
        self.commands = {
            "quit": lambda args: sys.exit()
        }

        #TODO: add operator's commands to self.commands
    
    def __run_interactively(self):
        ''' get user's input, then process command and print response'''
        while True:
            command = input(">>")
            if command not in self.commands.keys():
                print("command '{}' doesn't exist!".format(command))
            else:
                command, *arguments = command.split(" ")
                self.commands[command](arguments)
    def __run_cli(self):
        '''parse command line arguments, execute command and quit then'''
        pass

    def guard(fn):
        '''decorator to catch ctrl-C and other interruptions'''
        def inner(self):
            try:
                fn(self)
            except KeyboardInterrupt:
                sys.exit()
                os.clear()
        return inner
    

    @guard
    def run(self):
        '''the only public method. Call it to run app'''
        if len(sys.argv) > 1:
            self.__run_cli()
        else:
            self.__run_interactively()

        
