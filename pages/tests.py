from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_homepageview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Home')

