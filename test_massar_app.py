# test_selenium_app.py

import pytest
from selenium import webdriver

# Fixture to initialize the web driver before each test
@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()  # Replace with appropriate WebDriver (Chrome, Firefox, etc.)
    request.cls.driver = driver  # Make the driver available to the test class
    yield
    driver.quit()  # Close the browser after the test

# Test class for Selenium tests
@pytest.mark.usefixtures("setup")
class TestSeleniumApp:
    def test_title(self):
        self.driver.get("https://massar.men.gov.ma/Account")
        assert "Example Domain" in self.driver.title

    def test_search(self):
        self.driver.get("https://massar.men.gov.ma/Account")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("Selenium testing")
        search_box.submit()
        assert "Selenium testing" in self.driver.title
