"""
This selenium script is used to launch chrome browser with user profile using Chrome Options.
chrome_profile deprecated and combined with chrome options itself. 
***Note: Close all chrome browser instances before running this script***
"""
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from TestLocators import locators
import pytest

class TestChromeProfile:        
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        # Initialize Chrome options and add arguments
        chrome_options = Options()
        # use the path to your Chrome profile
        chrome_options.add_argument(locators.TestData.chrome_profile_path)

        # choose the profile you want to use
        chrome_options.add_argument('--profile-directory=Profile 2')

        # Initialize the WebDriver with the options
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

        # Create a single wait object
        self.wait = WebDriverWait(self.driver, 15)  
        yield
        self.driver.quit()

    # Test Case 1 - Using Chrome Options to launch browser with user profile
    def test_chrome_profile(self, booting_function):
        try:
            self.driver.get(locators.TestData.google_url)

            # If it shows sign-in, then user account not added while launching browser
            profile_image = self.wait.until(EC.visibility_of_element_located((By.XPATH, locators.TestSelectors.profile_icon_xpath)))
            
            # assert profile_image
            assert profile_image is not None
            print("Browser Launched with User Profile")

        except NoSuchElementException:
            print("Not Launched with User Profile")
 