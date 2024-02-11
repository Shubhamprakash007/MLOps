import logging
import os
from datetime import datetime

def setup_logging(log_file_path, log_format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", log_level=logging.INFO):
    """
    Configure logging with specified log file path, format, and level.

    Args:
        log_file_path (str): Path to the log file.
        log_format (str): Format of log messages.
        log_level (int): Logging level (default is INFO).
    """
    logging.basicConfig(
        filename=log_file_path,
        format=log_format,
        level=log_level
    )

# Example usage
if __name__ == "__main__":
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_path, exist_ok=True)
    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    setup_logging(LOG_FILE_PATH)
    logging.info("Logging initialized")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
