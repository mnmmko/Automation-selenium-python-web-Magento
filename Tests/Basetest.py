import pytest

import random
import string
@pytest.mark.usefixtures("browser")
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.driver = browser

    @staticmethod
    def generate_random_email():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        domain = random.choice(["gmail.com", "yahoo.com", "outlook.com"])
        return f"{username}@{domain}"