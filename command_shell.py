import sys
import os
from common_operator import Operator

class CommandShell:
    def __init__(self):
        #every command is repsented with lambda that takes list of argument(even if command doesn't require any additional data)
        self.commands = {
            "quit": lambda args: sys.exit()
        }

        #create common operator and add all commands to shell's available ones
        self.operator = Operator()
        for key in self.operator.commands.keys():
            self.commands[key] = self.operator.commands[key]

    def __execute_if_possible(self,command:str,arguments:list):
        if command not in self.commands.keys():
            print("command '{}' doesn't exist!".format(command))
        else:
            self.commands[command](arguments)

    def __run_interactively(self):
        ''' get user's input, then process command and print response'''
        while True:
            command = input(">>")
            command, *arguments = command.split(" ")
            self.__execute_if_possible(command,arguments)
    def __run_cli(self):
        '''parse command line arguments, execute command and quit then'''
        command, *arguments = sys.argv[1:]
        self.__execute_if_possible(command,arguments)
        
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

        
