from PageObjectLibrary import PageObject
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class LoginPage(PageObject):
    PAGE_TITLE = "ToolsQA"
    PAGE_URL = "/automation-practice-form"

    _locators = {
        "first_name": "id=firstName",
        "last_name": "id=lastName",
        "email": "id=userEmail",
        "number": "id=userNumber",
        "date_of_birth": "id=dateOfBirthInput",
    }

    def fill_form(self):
        config = BuiltIn().get_variable_value("${CONFIG}")
        self.fill_first_name(config.first_name)
        self.fill_last_name(config.last_name)
        self.fill_email(config.email)
        self.click_gender()
        self.fill_number(config.number)
        self.select_date()
        self.fill_subjects()
        self.click_hobbies()
        self.fill_picture()
        self.fill_address()
        self.select_state()
        self.select_city()
        self.submit_form()
    
    def user_clicks_submit_button(self):
        self.submit()
    
    def fill_first_name(self, first_name):
        self.selib.input_text(self.locator.first_name, first_name)
    
    def fill_last_name(self, last_name):
        self.selib.input_text(self.locator.last_name, last_name)

    def fill_email(self, email):
        self.selib.input_text(self.locator.email, email)
    
    def fill_number(self, number):
        self.selib.input_text(self.locator.number, number)
    
    def fill_date(self, date):
        self.selib.input_text(self.locator.date_of_birth, "")
        self.selib.input_text(self.locator.date_of_birth, date);
    
    def click_gender(self):
        self.driver.find_element_by_xpath("//label[@for='gender-radio-1']").click()
    
    def select_date(self):
        self.driver.find_element_by_xpath("//input[@id='dateOfBirthInput']").click()
        self.driver.find_element_by_xpath("//select[@class='react-datepicker__month-select']/option[text()='April']").click()
        self.driver.find_element_by_xpath("//select[@class='react-datepicker__year-select']/option[text()='1984']").click()
        self.driver.find_element_by_xpath("//div[@class='react-datepicker__day react-datepicker__day--024']").click()
    
    def fill_subjects(self):
        subjects = self.driver.find_element_by_id("subjectsInput")
        subjects.send_keys("English")
        subjects.send_keys(Keys.TAB)
    
    def click_hobbies(self):
        self.driver.find_element_by_xpath("//label[@for='hobbies-checkbox-1']").click()
    
    def fill_picture(self):
        self.driver.find_element_by_id("uploadPicture").send_keys("/tmp/AvatarMegaman.png")
    
    def fill_address(self):
        self.driver.find_element_by_id("currentAddress").send_keys("My Address")
    
    def select_state(self):
        select = self.driver.find_element_by_id("react-select-3-input")
        select.send_keys("NCR")
        select.send_keys(Keys.TAB)
    
    def select_city(self):
        select = self.driver.find_element_by_id("react-select-4-input")
        select.send_keys("Gurgaon")
        select.send_keys(Keys.TAB)

    def submit_form(self):
        self.driver.find_element_by_id("submit").click()

    def the_modal_should_have_the_text(self, text):
        wait = WebDriverWait(self.driver, 2)
        wait.until(ec.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg")))
        if self.driver.find_element_by_id("example-modal-sizes-title-lg").text != text:
            raise AssertionError("Modal doesn't have the text {}".format(text))