from selenium import webdriver

class DriverManager:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            # options.add_argument("--headless")  # optional
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--allow-insecure-localhost")
            options.add_argument("--test-type")
            options.add_argument("--disable-Features=IsolateOrigins,site-per-process")
            options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://live.techpanda.org")
            options.add_argument("--disable-client-side-phishing-detection")
            options.add_argument("--disable-popup-blocking")
            cls._driver = webdriver.Chrome(options=options)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
