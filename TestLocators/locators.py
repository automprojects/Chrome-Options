class TestData:
    # url constants
    google_url = "https://www.google.com"

    # Note: add '--user-data-dir=' before chrome profile path
    chrome_profile_path = "--user-data-dir=C:\\Users\\Folder\\AppData\\Local\\Google\\Chrome\\User Data"

# Python Class for Selenium Selectors
class TestSelectors:
    # Selectors for BrowserStack
    downloadcsv_xpath = '//a[@class="icon-csv"]'

    # Selectors for Google
    profile_icon_xpath = '//img[contains(@src, "lh3.googleusercontent.com")]'