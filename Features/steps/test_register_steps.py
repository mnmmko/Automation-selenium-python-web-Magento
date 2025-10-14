from Pages.Homepage import Homepage
from Pages.Registerpage import RegisterPage
from pytest_bdd import scenarios, given, when, then, parsers
from pathlib import Path
from Tests.Basetest import BaseTest
from common.DriveManeger import DriverManager

FEATURE_PATH = Path(__file__).parent.parent / "register.feature"
scenarios(str(FEATURE_PATH))


@given("user in register page")
def open_register_page():
    driver = DriverManager.get_driver()
    hp = Homepage(driver)
    hp.clickaccount()
    hp.clickregister()


@when(parsers.parse('user enter fname "{fname}" and mname "{mname}" and lname "{lname}" and password "{password}" and conpass "{conpass}"'))
def fill_register_field(fname, mname, lname, password, conpass):
    driver = DriverManager.get_driver()
    rp = RegisterPage(driver)
    rp.addfname(fname)
    rp.addmiddlename(mname)
    rp.addlname(lname)
    rp.addemail(BaseTest.generate_random_email())
    rp.addpassword(password)
    rp.addconfirmation(conpass)
    rp.clickcheck_is_registered()


@when("click register button")
def click_register():
    driver = DriverManager.get_driver()
    rp = RegisterPage(driver)
    rp.clickregister()


@then("register successfully")
def check_register():
    driver = DriverManager.get_driver()
    hp = Homepage(driver)
    assert "Thank you for registering with Main Website Store." in hp.get_success_sub()


