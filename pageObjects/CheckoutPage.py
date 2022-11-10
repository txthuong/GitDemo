from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    products = (By.XPATH, "//div[@class='card h-100']")
    cardTitle = (By.CLASS_NAME, "card-title")
    cardButton = (By.XPATH, ".//button[@class='btn btn-info']")

    # self.driver.find_element(By.XPATH, "//li/a[@class='nav-link btn btn-primary']").click()
    # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    checkOut = (By.XPATH, "//li/a[@class='nav-link btn btn-primary']")
    checkoutSuccessButton = (By.XPATH, "//button[@class='btn btn-success']")


    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getCardTitle(self, product):
        return product.find_element(*CheckoutPage.cardTitle)

    def getCardButton(self, product):
        return product.find_element(*CheckoutPage.cardButton)

    def checkOutItems(self):
        self.driver.find_element(*CheckoutPage.checkOut).click()
        self.driver.find_element(*CheckoutPage.checkoutSuccessButton).click()
        return ConfirmPage(self.driver)

