import sys
def error_msg_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    error_msg="error in [{0}] at line [{1}] error [{2}]".format(exc_tb.tb_frame.f_code.co_filename,exc_tb.tb_lineno,str(error))
    return error_msg

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_msg_details(error_message,error_details)
        
    def __str__(self):
        return self.error_message    
        