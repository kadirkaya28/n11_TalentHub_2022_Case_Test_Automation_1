from config.config import TestData
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from helper.helper import csv_writer, text_similarity_ratio


class CampaignPage(BasePage):
    HEADER = (By.TAG_NAME, "h2")
    CAMPAIGNS_FIELD = (By.TAG_NAME, "li > a")
    NAVBAR_ELEMENTS = (By.CSS_SELECTOR, ".campPromTab > li")
    CATEGORY_SECTION = (By.CSS_SELECTOR, "section[data-category]")

    def __init__(self, driver):
        super().__init__(driver)
        self.navigate_to_url(TestData.BASE_URL)

    def get_navbar_elements(self, locator) -> list:
        return self.find_elements(locator)

    def click_navbar_element_and_get_text(self, element: WebElement) -> str:
        attribute = self.get_attribute(element, "data-cat")
        text = self.get_element_text(element) if attribute is None else attribute
        text = text.lower().replace("ü", "u")
        self.mark_element(element, "red")
        self.click(element)
        return text

    def get_selected_category_section(self, locator, text) -> WebElement:
        elements = self.find_elements(locator)
        for element in elements:
            if text_similarity_ratio(text, self.get_attribute(element, "data-category")) > 65:
                return element

    def get_campaign_list(self, element: WebElement):
        camp_list = element.find_elements(*self.CAMPAIGNS_FIELD)
        header = element.find_element(*self.HEADER)
        self.scroll(header)
        self.static_wait(3)
        self.mark_element(header, "red")
        return camp_list, header.text

    def get_elements_url(self, elements: list) -> list:
        url_list = []
        for element in elements:
            url_list.append([self.get_attribute(element, "title"),
                             self.get_attribute(element, "href")])
        return url_list

    @staticmethod
    def create_csv_file(file_name: str, header: str, url_list: list) -> None:
        csv_writer(file_name, header, url_list)
