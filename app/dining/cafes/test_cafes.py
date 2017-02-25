from django.test import TestCase, Client    
from django.core.urlresolvers import reverse
from cafes import models


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
        def test_cafe_list(self):
            response = self.client.get(reverse('cafe_list'))
            self.assertEqual(response.status_code, 200)
        
        def test_cafe_detail(self):
            url = reverse('meal_detail', args=[self.test_cafe.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

        def fails_invalid(self):
            response = self.client.get(reverse('cafe_list'))
            self.assertEquals(response.status_code, 404)

        def tearDown(self):
            pass #nothing to tear down
   

