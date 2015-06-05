from selenium import webdriver
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_slideshow_initial_image_goes_to_model_page(self):
		# Check out the home page
		self.browser.get(self.live_server_url)

		# Check page title and header mention website name
		self.assertIn('WeatherPoint', self.browser.title)

		# Check first slide image goes to model page
		self.browser.find_element_by_id('modelspg').click()
		self.assertIn('Models', self.browser.title)

		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')


