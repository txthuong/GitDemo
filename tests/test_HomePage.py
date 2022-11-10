import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, get_data):
        log = self.get_logger()
        #name = "txthuong"
        #password = "123456"
        #email = "txthuong@gmail.com"
        #gender = "Male"
        employment_status = "Employed"
        #birthday = "01/01/1991"

        home_page = HomePage(self.driver)
        home_page.set_name(get_data["name"])
        log.info("Running with name:"+get_data["name"])
        home_page.set_password(get_data["password"])
        home_page.set_email(get_data["email"])
        home_page.select_checkbox()
        self.select_dropdown_by_text(home_page.get_gender(), get_data["gender"])
        home_page.select_employment_status(employment_status)
        home_page.set_birthday(get_data["bday"])
        home_page.submit()

        alert_message = home_page.get_alert_message()
        log.info(alert_message)
        if "Success!" in alert_message:
            print("%s: Test PASSED !!!" % get_data["name"])
        else:
            print("%s: Test FAILED !!!" % get_data["name"])

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.get_test_data("TestCase02"))
    def get_data(self, request):
        return request.param

