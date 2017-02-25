		from django.test import TestCase, Client
    from django.core.urlresolvers import reverse
    from cafes import models

    class GetCafeTestCase(TestCase):
        #setUp method is called before each test in this class
        def setUp(self):
            pass #nothing to set up

        def test_success_response(self):
        	post_data = {'name':'TestCafe','location':'Runk','date':'01.02.2017','description':'test','Calories':'300'}
        	c = Client()
        	response = c.post('/api/v1/meals/create', post_data)
        	i = json.loads((response.content).decode("utf-8"))
        	self.assertEquals(json_obj["ok"], True) 

        def tearDown(self):
            pass #nothing to tear down
   
