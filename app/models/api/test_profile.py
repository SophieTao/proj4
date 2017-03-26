# from django.test import TestCase, Client    
# from django.core.urlresolvers import reverse
# from api import models
# from .models import Cafe, Comment, Profile
# import json

# class ProfileTestCase(TestCase):
#         #setUp method is called before each test in this class
#         def setUp(self):
#            self.test_profile = Profile.objects.create(
#                 username = "Cathy",
#             )
#         def test_invalid_url(self):
#             response = self.client.get('/profile/')
#             self.assertEquals(response.status_code, 404)

#         def test_valid_profile_detail(self):
#             url = reverse('retrieve_update_profiles', args=[self.test_profile.id])
#             response = self.client.get(url)
#             self.assertEqual(response.status_code, 200)
#             resp_json = json.loads((response.content).decode("utf-8"))
#             self.assertEquals(resp_json["username"] , "Cathy")
            
#         def test_invalid_profile_detail(self):
#             response = self.client.get(reverse('retrieve_update_profiles', args=[10000]))
#             resp_json = (response.content).decode("utf-8")
#             self.assertEqual(resp_json, '"Profile does not exist."')
        
#         def test_valid_create_profile(self):
#             data = {"username": "Dan"}
#             response = self.client.post(reverse("profile-add"), data)
#             resp_json = json.loads((response.content).decode("utf-8"))
#             self.assertEquals(resp_json["username"] , "Dan")
            
#         def test_invalid_create_profile1(self):
#             wrongdata = {"description":"hello"}
#             response = self.client.post(reverse('profile-add'), wrongdata)
#             resp_json = (response.content).decode("utf-8")
#             self.assertEquals(resp_json, '"Input did not contain all the required fields."')
        
#         def test_invalid_create_profile2(self):
#             wrongdata = {}
#             response = self.client.post(reverse('profile-add'), wrongdata)
#             resp_json = (response.content).decode("utf-8")
#             self.assertEquals(resp_json, '"Input did not contain all the required fields."')

#         def test_valid_edit_profile(self):
#             response = self.client.post(reverse('retrieve_update_profiles', args=[self.test_profile.id]), {'username': "notCathy"})
#             resp_json = json.loads((response.content).decode("utf-8"))
#             self.assertEquals(resp_json["username"] , "notCathy")

#         def test_invalid_edit_profile(self):
#             wrongdata = {"username": "test_invalid_edit"}
#             response = self.client.post(reverse('retrieve_update_profiles', args=[10000]), wrongdata)
#             resp_json = (response.content).decode("utf-8")
#             self.assertEquals(resp_json, '"Profile does not exist."')

#         def test_valid_delete_profile(self):
#             deleteresponse = self.client.post(reverse('profile-delete', args=[self.test_profile.id]))
#             resp_json = (deleteresponse.content).decode("utf-8")
#             self.assertEquals(resp_json, '"Deleted profile "')
#             #duplicate deletes
#             deleteresponse2 = self.client.post(reverse('profile-delete', args=[self.test_profile.id]))
#             resp2_json = (deleteresponse2.content).decode("utf-8")
#             self.assertEquals(resp2_json, '"This profile does not exist."')

#         def test_invalid_delete_profile(self):
#             response = self.client.post(reverse('profile-delete', args=[10000]))
#             resp_json = (response.content).decode("utf-8")
#             self.assertEquals(resp_json, '"This profile does not exist."')

#         def tearDown(self):
#             pass #nothing to tear down


        

