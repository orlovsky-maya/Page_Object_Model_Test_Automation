import datetime
import os
import pytest


class Logger:
    def __new__(cls, directory):
        if not hasattr(cls, 'instance'):
            logger = super(Logger, cls).__new__(cls)
            now_date = datetime.datetime.utcnow().strftime("%Y_%m_%d.%H.%M.%S")
            logger.file_name = f"{directory}/Logs/log_{now_date}.log"

            cls.instance = logger
        return cls.instance

    def write_log_to_file(self, data: str):
        with open(self.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    def add_start_step(self, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        self.write_log_to_file(data_to_add)

    def add_end_step(self, url: str, method: str):
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        self.write_log_to_file(data_to_add)
