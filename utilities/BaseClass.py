import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_dropdown_by_text(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('D:/Course/PythonSelfFramework/utilities/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s: %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
