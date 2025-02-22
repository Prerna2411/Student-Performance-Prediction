import sys
from src.mlproject.logger import logging

def error_message_detail(error, error_detail: sys):
    """
    Constructs a detailed error message including the script name, line number, and error message.
    
    Args:
        error: The error message or exception object.
        error_detail: The sys module to capture exception details.
    
    Returns:
        str: A formatted error message.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class for more detailed error messages.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Args:
            error_message: The error message or exception object.
            error_detail: The sys module to capture exception details.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)