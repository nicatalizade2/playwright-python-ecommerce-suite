import logging
import os


def get_logger(name="QA_Automation"):
    logger = logging.getLogger(name)

    # Only add handlers if they don't exist (prevents duplicate logs)
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # 1. File Handler (Saves to test.log)
        file_handler = logging.FileHandler("test.log", mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # 2. Console Handler (Shows in PyCharm terminal)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger