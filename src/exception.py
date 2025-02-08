import sys
import logging

def error_msg_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in a python script name {0} line number {1} err msg {2}".format(
        filename,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_msg_details(error_message,error_detail)
        

    def __str__(self):
        return self.error_message