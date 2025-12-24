import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    _file_name = exc_tb.tb_frame.f_code.co_filename
    _line_no=exc_tb.tb_lineno
    _err_msg=str(error)
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(_file_name,_line_no,_err_msg)
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    