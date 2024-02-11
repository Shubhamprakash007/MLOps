import sys
import logging

def error_message_detail(error):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file '{file_name}', line {line_number}: {error}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message

    def __str__(self):
        return self.error_message
    
# def main():
#     try:
#         # Code that may raise an exception
#         raise CustomException("Custom error message")
#     except CustomException as e:
#         error_message = error_message_detail(e)
#         logging.error(error_message)

# if __name__ == "__main__":
#     main()