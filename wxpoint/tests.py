from django.test import TestCase
from django.core.urlresolvers import resolve
from wxpoint.views import home_page
from wxpoint.views import model_page
from django.http import HttpRequest
from django.template.loader import render_to_string
from wxpoint.models import NModels, ModelRun, ModelRegion, ModelImages
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

class NumModelTest(TestCase):
    #Refactor this test
    def test_saving_and_retrieving_items(self):
    	# Test first table stores model names
        first_model = NModels()
        first_model.name = 'GFS'
        first_model.save()

        second_model = NModels()
        second_model.name = 'CMC'
        second_model.save()

        saved_models = NModels.objects.all()
        self.assertEqual(saved_models.count(), 2)

        # Test saving multiple model runs
        gfs_model = ModelRun()
        gfs_model.currmodel = first_model
       	gfs_model.run_name = 'gfs2015060606'
       	gfs_model.save()
       	gfs_model2 = ModelRun()
       	gfs_model2.currmodel = first_model
       	gfs_model2.run_name = 'gfs2015060600'
       	gfs_model2.save()
       	saved_runs = ModelRun.objects.all()
       	self.assertEqual(saved_runs.count(), 2)

       	first_run_saved = saved_runs[0]
       	second_run_saved = saved_runs[1]
       	self.assertEqual(first_run_saved.run_name, 'gfs2015060606')
       	self.assertEqual(second_run_saved.run_name, 'gfs2015060600')

       	usa_region = ModelRegion()
       	usa_region.model_run = gfs_model
       	usa_region.region = 'USA'
       	usa_region.save()
       	NE_region = ModelRegion()
       	NE_region.model_run = gfs_model
       	NE_region.region = 'Northeast'
       	NE_region.save()
       	saved_regions = ModelRegion.objects.all()
       	self.assertEqual(saved_regions.count(), 2)

       	usa_region_saved = saved_regions[0]
       	ne_region_saved = saved_regions[1]
       	self.assertEqual(usa_region_saved.region, 'USA')
       	self.assertEqual(ne_region_saved.region, 'Northeast')

       	m_images = ModelImages()
       	m_images.model_region = usa_region
       	m_images.map_type = 'preciptype'
       	m_images.map_path = 'test.png'
       	m_images.timestep = '06'
       	m_images.save()
       	saved_images = ModelImages.objects.all()

       	model_image_saved = saved_images[0]
       	self.assertEqual(model_image_saved.map_type, 'preciptype')
       	self.assertEqual(model_image_saved.map_path, 'test.png')
       	self.assertEqual(model_image_saved.timestep, '06')







        
