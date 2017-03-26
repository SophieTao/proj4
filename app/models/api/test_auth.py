from django.test import TestCase, Client    
from django.core.urlresolvers import reverse
from api import models
from .models import Cafe, Comment, Profile, Authenticator
import json

class AuthenticatorTestCase(TestCase):
        #setUp method is called before each test in this class
        def setUp(self):
           # self.test_auth = Authenticator.objects.create(
           #      user_id = '71',
           #      authenticator='10cf2d282e41886b94f7c9388588b89c2cb3a4686cc00264b758dbb7f1d4721e',
           #      date_created="2017-03-25T20:44:23.240",
           #  )
           self.test_auth = Profile.objects.create(
                username = 'test',
                password='test',
                email="test@gmail.com",
            )
        def test_invalid_url(self):
            response = self.client.get('/auth/')
            self.assertEquals(response.status_code, 404) 

        def test_valid_all_auth(self):
            response = self.client.get(reverse('get_all_auth'))
            self.assertEqual(response.status_code, 200)

        # def test_valid_create_auth(self):

        #     response = self.client.get(reverse('comment_list'))
        #     self.assertEqual(response.status_code, 200)

        # def test_valid_comment_detail(self):
        #     url = reverse('retrieve_update_comments', args=[self.test_comment.id])
        #     response = self.client.get(url)
        #     self.assertEqual(response.status_code, 200)
        #     resp_json = json.loads((response.content).decode("utf-8"))
        #     self.assertEquals(resp_json["feedback"] , "fake feedback")
        #     self.assertEquals(resp_json["date_written"] , "2017-02-14T21:19:07.831Z")
        #     self.assertEquals(resp_json["description"] , "fake comment")
        #     self.assertTrue(str(resp_json["rating"]) == "1")
            
        # def test_invalid_comment_detail(self):
        #     response = self.client.get(reverse('retrieve_update_comments', args=[10000]))
        #     resp_json = (response.content).decode("utf-8")
        #     self.assertEqual(resp_json, '"Comment does not exist."')
        
#         def test_valid_create_auth(self):
#             data = {"username": "Dan", "password": "Bob"}
# #             response = self.client.post(reverse("profile-add"), data)
# #             resp_json = json.loads((response.content).decode("utf-8"))
# #             self.assertEquals(resp_json["username"] , "Dan")
#             data = {"username": "Bob", "password": "Bob"}
#             response = self.client.post(reverse("create_auth"), data)
#             # resp_json = json.loads((response.content).decode("utf-8"))
#             # self.assertTrue(resp_json["authenticator"])
#             # self.assertTrue(resp_json["date_created"])
#             # self.assertTrue(resp_json["user_id"])
#             resp_json = (response.content).decode("utf-8")
#             self.assertEquals(resp_json, '"User Does Nots Exist"')    

        def test_valid_create_auth(self):
            data = {"username": "Dan", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse("create_auth"), data)            
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, '"User Does Not Exist"')    
            response = self.client.post(reverse("profile-add"), data)
            response2 = self.client.post(reverse("create_auth"), data)            
            resp_json2 = json.loads((response2.content).decode("utf-8"))
            self.assertTrue(resp_json2["authenticator"])
            self.assertTrue(resp_json2["date_created"])
            self.assertTrue(resp_json2["user_id"])

        def test_invalid_create_auth_pw(self):
            data = {"username": "Dan", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse("profile-add"), data)
            response2 = self.client.post(reverse("create_auth"), data) 
            wrongdata = {"username": "Dan", "password": "Dan1", "email": "Dan@gmail.com"}
            response = self.client.post(reverse('create_auth'), wrongdata)
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, '"Incorrect password"')

        def test_invalid_create_auth_name(self):
            data = {"username": "Dan", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse("profile-add"), data)
            response2 = self.client.post(reverse("create_auth"), data) 
            wrongdata = {"username": "Dan1", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse('create_auth'), wrongdata)
            resp_json = (response.content).decode("utf-8")
            self.assertEquals(resp_json, '"User Does Not Exist"')
        
        def test_invalid_check_auth(self):
            data = {"username": "Dan", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse("profile-add"), data)
            response2 = self.client.post(reverse("create_auth"), data)
            wrongdata = {"username": "Dan1", "password": "Dan", "email": "Dan@gmail.com"}
            response3 = self.client.post(reverse("check_auth"), wrongdata)
            resp_json = (response3.content).decode("utf-8")
            self.assertEquals(resp_json, '"Authenticator does not exist."')

        def test_valid_check_auth(self):
            data = {"username": "Dan", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse("profile-add"), data)
            response2 = self.client.post(reverse("create_auth"), data)
            response3 = self.client.post(reverse("check_auth"), data)
            resp_json = json.loads((response3.content).decode("utf-8"))
            self.assertTrue(resp_json["authenticator"])
            self.assertTrue(resp_json["date_created"])
            self.assertTrue(resp_json["user_id"])

        def test_delete_auth(self):
            data = {"username": "Dan", "password": "Dan", "email": "Dan@gmail.com"}
            response = self.client.post(reverse("profile-add"), data)
            response2 = self.client.post(reverse("create_auth"), data)
            resp_json2 = json.loads((response2.content).decode("utf-8"))
            # response = self.client.post(reverse('create_auth'), data)
            # resp_json = json.loads((response.content).decode("utf-8"))
            # auth = resp_json["authenticator"]
            response3 = self.client.post(reverse('delete_auth'), resp_json2["authenticator"])
            resp_json3 = (response3.content).decode("utf-8")
            self.assertEquals(resp_json3, '"Successfully deleted user authentication"')
            response4 = self.client.post(reverse('delete_auth'), resp_json["authenticator"])     
            resp_json4 = (response4.content).decode("utf-8")
            self.assertEquals(resp_json4, '"User has not been authenticated yet."')

     # def test_invalid_create_comment3(self):
        #     wrongdata = {"date_written": "2017-02-14 21:19:07.831174","description": "I like today's lunch", "feedback": "thanks"}
        #     response = self.client.post(reverse('comment-add'), wrongdata)
        #     resp_json = (response.content).decode("utf-8")
        #     self.assertEquals(resp_json, '"Input did not contain all the required fields."')

        # def test_invalid_create_comment4(self):
        #     wrongdata = {"date_written": "2017-02-14 21:19:07.831174","description": "I like today's lunch", "rating": 3}
        #     response = self.client.post(reverse('comment-add'), wrongdata)
        #     resp_json = (response.content).decode("utf-8")
        #     self.assertEquals(resp_json, '"Input did not contain all the required fields."')

        # def test_valid_edit_comment(self):
        #     response = self.client.post(reverse('retrieve_update_comments', args=[self.test_comment.id]), {'feedback': "test_update_comment", "date_written":"2017-02-14 21:19:07.831174","description":"test","rating":3})
        #     resp_json = json.loads((response.content).decode("utf-8"))
        #     self.assertEquals(resp_json["feedback"] , "test_update_comment")
        #     self.assertEquals(resp_json["date_written"] , "2017-02-14 21:19:07.831174")
        #     self.assertEquals(resp_json["description"] , "test")
        #     self.assertTrue(str(resp_json["rating"]) == "3")
        #     #self.assertEquals(resp_json, "Updated task")

        # def test_invalid_edit_comment(self):
        #     wrongdata = {"name": "test_create_comment","location": "hello","date_written":"2017-02-14","description":"test","Calories":"300"}
        #     response = self.client.post(reverse('retrieve_update_comments', args=[10000]), wrongdata)
        #     resp_json = (response.content).decode("utf-8")
        #     self.assertEquals(resp_json, '"Comment does not exist."')

        # def test_valid_delete_comment(self):
        #     deleteresponse = self.client.post(reverse('comment-delete', args=[self.test_comment.id]))
        #     resp_json = (deleteresponse.content).decode("utf-8")
        #     self.assertEquals(resp_json, '"Deleted comment "')
        #     #duplicate deletes
        #     deleteresponse2 = self.client.post(reverse('comment-delete', args=[self.test_comment.id]))
        #     resp2_json = (deleteresponse2.content).decode("utf-8")
        #     self.assertEquals(resp2_json, '"This comment does not exist."')

        # def test_invalid_delete_comment(self):
        #     response = self.client.post(reverse('comment-delete', args=[10000]))
        #     resp_json = (response.content).decode("utf-8")
        #     self.assertEquals(resp_json, '"This comment does not exist."')

        def tearDown(self):
            pass #nothing to tear down


        

