from django.test import TestCase, Client    
from django.core.urlresolvers import reverse
from api import models
from .models import Cafe, Comment, Profile
import json

class MealTestCase(TestCase):
        #setUp method is called before each test in this class
        def setUp(self):
           self.test_cafe = Cafe.objects.create(
                name = 'test',
                location='Runk',
                date='2017-02-14 21:19:07.831174',
                description='test',
                Calories = '300',
            )
        def test_invalid_url(self):
            response = self.client.get('/cafe/')
            self.assertEquals(response.status_code, 404)

        def test_valid_meal_list(self):
            response = self.client.get(reverse('cafe_list'))
            self.assertEqual(response.status_code, 200)

        def test_valid_meal_detail(self):
            url = reverse('retrieve_update_cafes', args=[self.test_cafe.id])
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

        def test_invalid_meal_detail(self):
            response = self.client.get(reverse('retrieve_update_cafes', args=[10000]))
            resp_json = (response.content).decode("utf-8")
            self.assertEqual(resp_json, '"Cafe does not exist."')
        
        # def test_valid_create_meal(self):
        #     data = {"name": "test_create_meal","date":"2017-02-14 21:19:07.831174","description":"test","Calories":3000}
        #     response = self.client.post(reverse("cafe-add"), data)
        #     resp_json = json.loads((response.content).decode("utf-8"))
        # #   self.assertEquals(resp_json["name"] , "test_create_meal")
        #     self.assertIn("test_create_meal",resp_json)
            
        def test_invalid_create_meal(self):
            response = self.client.post(reverse('cafe-add'), {'name': "test_create_meal","date":"2017-02-14 21:19:07.831174","description":"test","Calories":3000}, format='json')
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, '"Input did not contain all the required fields."')

        # def test_valid_edit_meal(self):
        #     c= Cafe.objects.create(name = 'test',
        #         location='Runk',
        #         date='2017-02-14 21:19:07.831174',
        #         description='test',
        #         Calories = '300',)
        #     response = self.client.post(reverse('cafe-add'), c)
        #     resp_json = (response.content).decode("utf-8")
        #     response2 = self.client.post(reverse('retrieve_update_cafes', args=[c.id]), {'name': "test_update_meal","date":"2017-02-14 21:19:07.831174","description":"test","Calories":3000}, format='json')
        #     self.assertEquals(resp_json, "Updated task")

        def test_invalid_edit_meal(self):
            response = self.client.post(reverse('retrieve_update_cafes', args=[self.test_cafe.id]), {"date":"2017-02-14 21:19:07.831174","description":"test","Calories":3000}, format='json')
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, '"Did not update this task successfully"')

         
        # def test_valid_delete_meal(self):
        #     deleteresponse = self.client.delete(reverse('cafe-delete', args=[10]))
        #     resp_json = (deleteresponse.content).decode("utf-8")
        #     self.assertEquals(resp_json, '"Deleted meal"')

        #     deleteresponse2 = self.client.get(reverse('cafe-delete', args=[10]))
        #     resp2_json = (deleteresponse2.content).decode("utf-8")
        #     self.assertEquals(resp2_json, '"This meal does not exist."')

        def test_invalid_delete_meal(self):
            response = self.client.delete(reverse('cafe-delete', args=[10000]))
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, '"This meal does not exist."')

        def tearDown(self):
            pass #nothing to tear down


        

