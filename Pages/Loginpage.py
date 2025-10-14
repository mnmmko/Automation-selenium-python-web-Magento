from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    login_title = (By.TAG_NAME,"h1")
    emails = (By.ID,"email")
    password = (By.ID,"pass")
    login = (By.XPATH,"//button[@title='Login']")


    def get_login_title(self):
        return self.get_text(self.login_title)

    def enter_email(self,email):
        self.type(self.emails, email)



    def enter_password(self,passwords):
        self.type(self.password,passwords)



    def click_login(self):
        self.clickbtn(self.login)

    def get_email_validtied(self,attr):
        return self.get_attribute(self.emails,attr)




