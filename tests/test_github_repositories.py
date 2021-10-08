import json
import time

import requests

from pageObjects.GitHubHomePage import GitHubHomePage
from tests.conftest import _capture_screenshot
from utilities.BaseClass import BaseClass


class TestGitHubRepositories(BaseClass):

    def test_github_repo(self):
        try:
            log = self.getLogger()
            log.info("Logger object created")

            log.info("Page Object for HomePage initialised")
            gitHubHomePage = GitHubHomePage(self.driver)

            log.info('Navigating to Repository')
            gitHubHomePage.get_repository_tab_element().click()

            assert True == gitHubHomePage.get_repository_selected()

            log.info('Present on Repository Tab')
            actual_data_dict = gitHubHomePage.get_all_list()

            log.info('Print actual data of dictionary')
            log.info(actual_data_dict)

            log.info("Calling Rest Endpoint to get repositories")
            base_url = 'https://api.github.com'
            response_body = requests.get(base_url+'/orgs/django/repos')
            res_string = json.loads(response_body.text)

            log.info("Parsing Endpoint response for validation")
            expected_data_dict = {}
            for response in res_string:
                expected_data_dict[response.get("name")] = response.get("description")

            log.info("Asserting endpoint response with actual values from web")
            assert expected_data_dict == actual_data_dict

            log.info("Asserting status code for api respone")
            assert response_body.status_code == 200
            assert response_body.headers.get('Content-Type') == 'application/json; charset=utf-8'

        except:
            _capture_screenshot("TestGitHubRepositoriesFailedCase.png")
