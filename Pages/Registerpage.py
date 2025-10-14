from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    fname = (By.ID,"firstname")
    mname = (By.ID,"middlename")
    lname = (By.ID,"lastname")
    email = (By.ID,"email_address")
    password = (By.ID,"password")
    confirmpassword = (By.ID,"confirmation")
    check_is_registered = (By.ID,"is_subscribed")
    register = (By.XPATH,"//button[@title='Register']")
    back = (By.XPATH,"//a[@class='back-link']")

    def addfname(self,firstname):
        self.type(self.fname, firstname)



    def addmiddlename(self,middlename):
        self.type(self.mname, middlename)



    def addlname(self,lastname):
        self.type(self.lname, lastname)


    def addemail(self,emails):
        self.type(self.email, emails)

    def addpassword(self,passwords):
        self.type(self.password, passwords)


    def addconfirmation(self, confirmation):
        self.type(self.confirmpassword, confirmation)


    def clickcheck_is_registered(self):
        self.clickbtn(self.check_is_registered)

    def clickregister(self):
        self.clickbtn(self.register)

    def clickback(self):
        self.clickbtn(self.back)
