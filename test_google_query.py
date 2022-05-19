import unittest, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class SmokeTest(unittest.TestCase):

    def setUp(self):
      #Required to run Seleniun on Repl.it
      chrome_options = Options()
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')
      self.driver = webdriver.Chrome(options=chrome_options)
      self.driver.get("http://google.com")

    def tearDown(self):
        self.driver.quit()

    def test_can_query_on_google(self):
        element = self.driver.find_element_by_name("q")
        element.send_keys("software testing")
        element.submit()
        time.sleep(3)

        self.assertIn("software testing", self.driver.title)
        self.assertIn("https://www.google.com/search?q=software+testing", self.driver.current_url)
        self.driver.get("http://bing.com")
        time.sleep(3)
        self.assertIn("https://www.bing.com", self.driver.current_url)
        element = self.driver.find_element_by_name("q")
        element.send_keys("hardware")
        element.submit()
        time.sleep(3)
        self.assertIn("hardware", self.driver.title)
        