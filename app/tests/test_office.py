import unittest
import json
from app import create_app
from app.api.v1.view.office_views import Offices, Office

app = create_app('testing')
class Testoffice(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.test_office = {
            'name':'Governor',
            'age':'35',
            'office_type':'county',
            'education':'O-level'
        }
        self.test_office_missing_name = {
            'name':'',
            'age':'35',
            'office_type':'county',
            'education':'O-level'
        }
        self.test_office_missing_office_type = {
            'name':'Governor',
            'age':'35',
            'office_type':'',
            'education':'O-level'
        }
        self.test_office2 = {
            'name':'President',
            'age':'21',
            'offie_type':'state',
            'education':'Degree'
        }

        
    def test_create_office(self):
         response = self.app.post('/api/v1/offices',
                     data = json.dumps(self.test_office),
                     headers = {'content-type':'application/json'}) 
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Successfully saved')
         self.assertEqual(response.status_code,200)

         response2 = self.app.post('/api/v1/offices',
                     data = json.dumps(self.test_office_missing_name),
                     headers = {'content-type':'application/json'}) 
         result = json.loads(response2.data)
         self.assertEqual(result['Message'],'Input is required')
         self.assertEqual(response2.status_code,200)

         response3 = self.app.post('/api/v1/offices',
                     data = json.dumps(self.test_office_missing_office_type),
                     headers = {'content-type':'application/json'}) 
         result = json.loads(response3.data)
         self.assertEqual(result['Message'],'Input is required')
         self.assertEqual(response3.status_code,200)


    def test_find_office_usingid(self):
        self.app.post('/api/v1/offices',
                     data = json.dumps(self.test_office2),
                     headers = {'content-type':'application/json'})
        response  = self.app.get('/api/v1/offices/1')
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'The office has been returned successfully')
        self.assertEqual(response.status_code,200)


    def test_remove_office_usingid(self):
        self.app.post('/api/v1/offices',
                  data = json.dumps(self.test_office2),
                  headers = {'content-type':'application/json'})
        response = self.app.delete('/api/v1/offices/1')
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Office successfully deleted')
        self.assertEqual(response.status_code,200)


    def test_find_all_offices(self):
        response = self.app.get('/api/v1/offices')
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Returned successfully')
        self.assertEqual(response.status_code,200)

    if __name__  ==  "__main__":
        unittest.main()
