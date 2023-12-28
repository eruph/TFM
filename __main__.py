if __name__ == '__main__':
    from command_shell import *

    #TODO: there is a chance chdir may throw exception, so check it
    #to make available using python TFM
    from os import chdir
    chdir("TFM")
    
    shell = CommandShell()
    shell.run()
