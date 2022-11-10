from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckoutPage import CheckoutPage



class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//div[@class='form-group']/input[@name='name']")
    email = (By.XPATH, "//div[@class='form-group']/input[@name='email']")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.XPATH, "//div[@class='form-check']/label[@class='form-check-label']")
    gender = (By.ID, "exampleFormControlSelect1")
    employment_status = (By.CSS_SELECTOR, "div[class='form-check form-check-inline']")
    birthday = (By.CSS_SELECTOR, "input[name='bday']")
    submit_button = (By.CSS_SELECTOR, "input[class='btn btn-success']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def set_name(self, text):
        self.driver.find_element(*HomePage.name).send_keys(text)

    def set_email(self, text):
        self.driver.find_element(*HomePage.email).send_keys(text)

    def set_password(self, text):
        self.driver.find_element(*HomePage.password).send_keys(text)

    def select_checkbox(self):
        self.driver.find_element(*HomePage.checkbox).click()

    def select_gender(self, text):
        self.driver.find_element(*HomePage.gender).click()
        gender_dropdown = Select(self.driver.find_element(*HomePage.gender))
        gender_dropdown.select_by_visible_text(text)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def select_employment_status(self, text):
        status = self.driver.find_elements(*HomePage.employment_status)
        for s in status:
            if s == text:
                s.click()

    def set_birthday(self, text):
        self.driver.find_element(*HomePage.birthday).send_keys(text)

    def submit(self):
        self.driver.find_element(*HomePage.submit_button).click()

    def get_alert_message(self):
        return self.driver.find_element(*HomePage.alert).text