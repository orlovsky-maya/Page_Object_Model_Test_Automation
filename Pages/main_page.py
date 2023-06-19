from Pages.base_page import BasePage


class MainPage(BasePage):
    LINK = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, browser):
        super().__init__(browser, self.LINK)
