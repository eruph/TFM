from DBManager import *
from typing import Callable, Any

#there should be only one instance of data base manager
class BaseOperator:
    def __init__(self):
        self.db = DBManager()

    #check and run if possible:for short 
    def crifp(self,args:list, required_args_amount:int, fn:Callable[..., Any]) -> bool:
        '''if len of passed arguments is equal to required one, then call function. otherwise print doc for the function'''
        if len(args) != required_args_amount:
            print(fn.__doc__)
        else:
            fn(*args)

    
    def _get_methods_iter(self, object:Any):
        isc = lambda fn: callable(getattr(object,fn)) #check is callable
        np  = lambda fn: not fn.startswith("__")      #check is not private
        npp = lambda fn: not fn.startswith("_")       #check is not protected

        #exlude crifp, because it's "special" method
        return (getattr(object,fn) for fn in dir(object) if isc(fn) and np(fn) and npp(fn) and fn != "crifp")

    def _set_docs(self,commands:dict):
        '''set __doc__ string for every command'''
        for method in self._get_methods_iter(self):
            for key in commands.keys():
                if key in method.__doc__:
                    commands[key].__doc__ = method.__doc__
