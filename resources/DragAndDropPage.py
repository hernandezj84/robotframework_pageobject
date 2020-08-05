from PageObjectLibrary import PageObject
from selenium.webdriver.common.action_chains import ActionChains


class DragAndDropPage(PageObject):
    PAGE_TITLE = "ToolsQA"
    PAGE_URL = "/droppable"

    def drag_and_drop_element(self):
        dragable = self.driver.find_element_by_id("draggable")
        droppable = self.driver.find_element_by_id("droppable")
        ActionChains(self.driver).drag_and_drop(dragable, droppable).perform()
    
    def verify_class_drop_element(self):
        if self.driver.find_element_by_id("droppable").get_attribute("class") != "drop-box ui-droppable ui-state-highlight":
            raise AssertionError("The element doesn't change its color")