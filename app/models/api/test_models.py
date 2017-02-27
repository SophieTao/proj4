from django.test import TestCase, Client    
from django.core.urlresolvers import reverse
from api import models
from django.core.management import call_command
from .models import Cafe, Comment, Profile

import json

class GetOrderDetailsTestCase(TestCase):
        #setUp method is called before each test in this class
        def setUp(self):
           self.test_cafe = models.Cafe.objects.create(
                name = 'test',
                location='Runk',
                date='2017-02-01',
                description='test',
                Calories = '300',
            )
        def test_meal_list(self):
            response = self.client.get(reverse('cafe_list'))

            self.assertEqual(response.status_code, 200)
        
        def test_meal_detail(self):
            url = reverse('meal_detail', args=[self.test_cafe.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

        def fails_invalid_url(self):
            response = self.client.get('/cafe/')
            self.assertEquals(response.status_code, 404)

        def fails_invalid_meal(self):
            response = self.client.get(reverse('meal_detail', args=[10]))
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, 'False')

        def tearDown(self):
            pass #nothing to tear down
   

