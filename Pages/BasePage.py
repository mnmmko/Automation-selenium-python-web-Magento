from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clickbtn(self, locator):
        elem=self.fluent_wait(locator,10,3)
        elem.click()

    def type(self, locator, text):
        elem = self.fluent_wait(locator,10,3)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator):
        # return self.wait.until(EC.visibility_of_element_located(locator)).text
        return self.fluent_wait(locator,10,3).text
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    def fluent_wait(self,lecator,time,freq):
        self.wait = WebDriverWait(self.driver, timeout=time, poll_frequency=freq, ignored_exceptions=None)
        return self.wait.until(EC.visibility_of_element_located(lecator))

    def double_click_element(self, locator):
        elem = self.fluent_wait(locator,10,3)
        actions = ActionChains(self.driver)
        actions.move_to_element(elem).double_click(elem).perform()

    def select_all_text(self, locator):
        elem = self.fluent_wait(locator, 10, 3)
        elem.click()
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

    def get_attribute(self, locator,attr):
        elem = self.fluent_wait(locator, 10, 3)
        return elem.get_attribute(attr)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        element = self.fluent_wait(locator, 10, 3)
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        return element