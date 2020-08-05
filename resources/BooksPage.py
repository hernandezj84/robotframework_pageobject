from PageObjectLibrary import PageObject


class BooksPage(PageObject):
    PAGE_TITLE = "ToolsQA"
    PAGE_URL = "/books"

    def find_search_box(self, text):
        self.driver.find_element_by_id("searchBox").send_keys(text)
    
    def number_of_books(self, number):
        lines = self.driver.find_elements_by_xpath("//span[@class='mr-2']")
        if len(lines) != int(number):
            raise AssertionError("Number of books isn't correct {} != {}".format(len(lines), number))

