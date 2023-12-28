import sys
import os


class CommandShell:
    def __init__(self):

        #every command is repsented with lambda that takes list of argument(even if command doesn't require any additional data)
        self.commands = {
            "quit": lambda args: sys.exit()
        }
        
    def __run_interactively(self):
        while True:
            command = input(">>")
            if command not in self.commands.keys():
                print("command '{}' doesn't exist!".format(command))
            else:
                command, *arguments = command.split(" ")
                self.commands[command](arguments)
    def __run_cli(self):
        pass


    def run(self):
        if len(sys.argv) > 1:
            self.__run_cli()
        else:
            self.__run_interactively()
        
