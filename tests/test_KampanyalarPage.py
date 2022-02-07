from tests import BaseTest
from config.config import TestData
from pages.CampaignPage import CampaignPage


class TestCampignPage(BaseTest):

    def test_campaign_page(self):
        campaign_page = CampaignPage(self.driver)
        assert TestData.CAMPAIGN_PAGE_TITLE in campaign_page.get_title()

        navbar_elements = campaign_page.get_navbar_elements(campaign_page.NAVBAR_ELEMENTS)

        for idx, element in enumerate(navbar_elements):

            assert TestData.NAVBAR_ELEMENTS[idx] in element.text

            if not campaign_page.is_disabled(element):

                text = campaign_page.click_navbar_element_and_get_text(element)
                category = campaign_page.get_selected_category_section(campaign_page.CATEGORY_SECTION, text)
                camp_list, header = campaign_page.get_campaign_list(category)
                assert TestData.HEADERS[idx] in header

                url_list = campaign_page.get_elements_url(camp_list)
                campaign_page.create_csv_file(f"campaigns.csv", header, url_list)
