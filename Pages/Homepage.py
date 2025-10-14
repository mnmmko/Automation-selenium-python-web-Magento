import time

from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    title=(By.TAG_NAME,"h2")
    subcribe=(By.XPATH,"//button[@title='Subscribe']")
    email=(By.XPATH,"//input[@type='email']")
    account = (By.XPATH,"//a//span[text()='Account']")
    login = (By.XPATH,"//a[@title='Log In']")
    logout = (By.XPATH,"//a[text()='Log Out']")
    register = (By.XPATH,"//a[text()='Register']")
    sendaway = (By.XPATH,"//button[text()='Send anyway']")
    msg_success = (By.XPATH,"//li[@class='success-msg']//ul//li//span")

    def get_name_of_title(self):
        return self.get_text(self.title)

    def add_email(self,emails):
        self.type(self.email,emails)

    def subcribe_click(self):
        self.clickbtn(self.subcribe)

    def get_success_sub(self):
        return self.get_text(self.msg_success)


    def clickaccount(self):
            self.clickbtn(self.account)


    def clicklogin(self):
            self.clickbtn(self.login)

    def clicklogout(self):
            self.clickbtn(self.logout)

    def clickregister(self):
            self.clickbtn(self.register)

    def clicksendaway(self):
        time.sleep(5)
        self.double_click_element(self.sendaway)
