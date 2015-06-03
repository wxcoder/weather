from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
    	self.browser.quit()

    def test_can_click_slideshow(self):
   		# Check out the home page
   		self.browser.get('http://localhost:8000')

   		# Check page title and header mention website name
   		self.assertIn('WeatherPoint', self.browser.title)
   		self.fail('Finish the test!')

   		# Opens the page to a slideshow

if __name__ == '__main__':
	unittest.main(warnings='ignore')


