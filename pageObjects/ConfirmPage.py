from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ConfirmPage:

    countryBox = (By.ID, "country")
    suggestCountries = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    alertBox = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def getCountryBox(self):
        return self.driver.find_element(*ConfirmPage.countryBox)

    def selectCountryFromSuggestCountries(self, country):
        # self.verifyLinkPresence(country)
        self.driver.find_element(By.LINK_TEXT, country).click()
        #wait = WebDriverWait(self.driver, 10)
        #wait.until(expected_conditions.presence_of_element_located(ConfirmPage.suggestCountries))
        #listSuggestedCountry = self.driver.find_elements(*ConfirmPage.suggestCountries)
        #for suggestCountry in listSuggestedCountry:
        #    if suggestCountry.text == country:
        #        suggestCountry.click()
        #        break

    def selectCheckBox(self):
        self.driver.find_element(*ConfirmPage.checkBox).click()

    def purchase(self):
        self.driver.find_element(*ConfirmPage.purchaseButton).click()

    def getAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alertBox).text
