from PageObjectLibrary import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class ModalPage(PageObject):
    PAGE_TITLE = "ToolsQA"
    PAGE_URL = "/modal-dialogs"

    def click_small_modal_button(self):
        self.driver.find_element_by_id("showSmallModal").click()
    
    def verify_the_text(self, text):
        wait = WebDriverWait(self.driver, 2)
        wait.until(ec.visibility_of_element_located((By.ID, "example-modal-sizes-title-sm")))
        if self.driver.find_element_by_id("example-modal-sizes-title-sm").text != text:
            raise AssertionError("Modal doesn't have the text {}".format(text))
