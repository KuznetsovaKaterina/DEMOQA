from selenium.webdriver.common.by import By

from generator.generator import generate_person
from pages.base import Base


# Locators TextBox
class TextBoxLocators:
    # locators for input
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # locators for output
    OUTPUT_NAME = (By.CSS_SELECTOR, "p[id='name']")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "p[id='email']")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "p[id='currentAddress']")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "p[id='permanentAddress']")


class TextBox(Base):
    def fill_data(self):
        person_data = generate_person()
        full_name = person_data.full_name
        email = person_data.email
        current_address = person_data.current_address
        permanent_address = person_data.permanent_address
        self.element_is_visible(TextBoxLocators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(TextBoxLocators.EMAIL).send_keys(email)
        self.element_is_visible(TextBoxLocators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(TextBoxLocators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(TextBoxLocators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_data(self):
        full_name = self.element_is_visible(TextBoxLocators.OUTPUT_NAME).text.split(':')[1]
        email = self.element_is_visible(TextBoxLocators.OUTPUT_EMAIL).text.split(':')[1]
        current_address = self.element_is_visible(TextBoxLocators.OUTPUT_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_visible(TextBoxLocators.OUTPUT_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
