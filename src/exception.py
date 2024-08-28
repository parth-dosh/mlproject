## for exception handling 


## we will be creating our own exceptions

import sys
# any exception that is being controlled will be handled by sys 
import logging # just to check whether exception.py is working 
from src.logger import logging

def error_message_detail(error, error_detail:sys): 
    _,_,exc_tb = error_detail.exc_info() # exc_info tells us which file the error has occured, which line it has occured and it is stored in our exc_tb info
    # we are not interested in the first two outputs of the exc_info() so we only store the third part 
    file_name = exc_tb.tb_frame.f_code.co_filename # this is given in custom exception handling docs 
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    # this above line basically gives us the file name, the line number and the error message that occurs when the error is raised 


    return error_message
    


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):  # initialize it with constructor 
        super().__init__(error_message)
        ## super.init because we are inheriting from the exception
        self.error_message = error_message_detail(error_message, error_detail=error_detail)


    ##firstly, it is raising the custom exception using the input parameter
    ## it is inheriting the parent exception 
    ## then it is initializing it to the class variable of the error message using self.error_message 

    def __str__(self): 
        return self.error_message  # used for printing the error message 
    




    



