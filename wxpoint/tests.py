from django.test import TestCase
from django.core.urlresolvers import resolve
from wxpoint.views import home_page
from wxpoint.views import model_page
from django.http import HttpRequest
from django.template.loader import render_to_string

from wxpoint.views import home_page
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		request = HttpRequest()
		response = home_page(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)

	def test_model_page_returns_correct_html(self):
		request = HttpRequest()
		response = model_page(request)
		expected_html = render_to_string('models.html')
		self.assertEqual(response.content.decode(), expected_html)
