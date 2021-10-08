from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class GitHubHomePage:

    def __init__(self, driver):
        self.driver = driver;

    repository = (By.CSS_SELECTOR, '[data-tab-item="org-header-repositories-tab"]')
    selected_repository = (By.CSS_SELECTOR, '[class$="selected"]')
    list_repositories_name = (By.CSS_SELECTOR, '[data-hovercard-type="repository"]')
    list_repositories_description = (By.CSS_SELECTOR, '[itemprop="description"]')

    all_list = (By.CSS_SELECTOR, '[itemprop="owns"]')

    def get_all_list(self):
        elements = self.driver.find_elements(*GitHubHomePage.all_list)
        data_dict = {}
        for element in elements:
            name = element.find_element(*GitHubHomePage.list_repositories_name).text
            try:
                description = element.find_element(*GitHubHomePage.list_repositories_description).text
            except NoSuchElementException:
                description = None
            data_dict[name] = description
        return data_dict

    def get_repository_tab_element(self):
        return self.driver.find_element(*GitHubHomePage.repository)

    def get_repository_selected(self):
        return self.get_repository_tab_element().find_element(*GitHubHomePage.selected_repository).is_displayed()
