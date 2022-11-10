from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.get_logger()

        buy_products = ["iphone X", "Blackberry"]
        country_char = "in"
        country = "India"

        home_page = HomePage(self.driver)
        checkout_page = home_page.shopItems()
        log.info("Getting all the card titles.")
        products = checkout_page.getProducts()

        for product in products:
            product_name = checkout_page.getCardTitle(product).text
            log.info(product_name)
            if product_name in buy_products:
                checkout_page.getCardButton(product).click()
                log.info(product_name + " added !!!")

        confirm_page = checkout_page.checkOutItems()
        log.info("Enter country name.")
        confirm_page.getCountryBox().send_keys(country_char)
        self.verifyLinkPresence(country)
        confirm_page.selectCountryFromSuggestCountries(country)
        confirm_page.selectCheckBox()
        confirm_page.purchase()
        alert_message = confirm_page.getAlertMessage()
        log.info("Text received: " + alert_message)
        if "Success" in alert_message:
            print("---> Passed !!!")
        else:
            print("---> Failed !!!")

