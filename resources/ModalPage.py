from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class ModalPage(PageObject):
    PAGE_TITLE = "ToolsQA"
    PAGE_URL = "/modal-dialogs"

    def click_small_modal_button(self):
        self.driver.find_element_by_id("showSmallModal").click()
    
    def verify_the_text(self, text):
        if self.driver.find_element_by_id("example-modal-sizes-title-sm").text != text:
            raise AssertionError("Modal doesn't have the text {}".format(text))


# "example-modal-sizes-title-sm"