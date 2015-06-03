from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
    	self.browser.quit()

    def test_slideshow_initial_image_goes_to_model_page(self):
   		# Check out the home page
   		self.browser.get('http://localhost:8000')

   		# Check page title and header mention website name
   		self.assertIn('WeatherPoint', self.browser.title)

   		self.browser.find_element_by_id('firstimg').click()

   		self.assertIn('Models Page', self.browser.title)

   		self.browser.find_element_by_id('home').click()
   		
   		self.assertIn('WeatherPoint', self.browser)

   		self.fail('Finish the test!')

   		# Opens the page to a slideshow


if __name__ == '__main__':
	unittest.main(warnings='ignore')


