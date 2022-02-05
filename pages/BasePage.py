import time
import allure
from time import ctime
from config.config import TestData
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    This class is the parent of all pages.
    It contains all the generic methods and utilities for all the pages
    """

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def navigate_to_url(self, url=TestData.BASE_URL):
        self.driver.get(url)

    @staticmethod
    def static_wait(timeout):
        time.sleep(timeout)

    def find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator) -> list[WebElement]:
        return WebDriverWait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator))

    def click(self, mark):
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        element.click()

    def scroll(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true)", element)

    def get_title(self) -> str:
        return self.driver.title

    def get_attribute(self, mark, attribute_name):
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        return element.get_attribute(attribute_name)

    def get_element_text(self, mark) -> str:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        return element.text

    def is_disabled(self, mark) -> bool:
        if isinstance(mark, WebElement):
            element = mark
        else:
            element = WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(mark))
        flag = self.get_attribute(element, "class") == " disabled "
        return flag

    def mark_element(self, element: WebElement, color: str, effect_time=1, thickness=2):
        original_style = element.get_attribute('style')

        set_style = lambda driver, style: driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                                                element, style)

        set_style(self.driver, f"border: {thickness}px solid {color};")
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=ctime(time.time()).replace(":", "_"),
                      attachment_type=AttachmentType.PNG)
        time.sleep(effect_time)
        set_style(self.driver, original_style)
