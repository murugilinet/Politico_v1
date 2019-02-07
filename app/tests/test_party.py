import unittest
import json
from app import create_app
from app.api.v1.view.party_views import Parties,Party

app = create_app('testing')
class Testparties(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.test_party1 = {
            'name':'Jogoo Party',
            'abbreviations':'JGP',
            'chairperson':'Suleiman',
            'members':'18',
            'address':'254789',
            'logoUrl':'logo'
            }
        self.test_party2 = {
             'name':'African Alliance',
            'abbreviations':'AFA',
            'chairperson':'Abdi',
            'members':'54',
            'address':'254123',
            'logoUrl':'logo'
            }

    def test_create_party(self):
         response = self.app.post('/api/v1/parties',
                     data = json.dumps(self.test_party1),
                     headers = {'content-type':'application/json'}) 
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Successfully saved')
         self.assertEqual(response.status_code,200)


    def test_find_party_usingid(self):
        self.app.post('/api/v1/parties',
                     data = json.dumps(self.test_party2),
                     headers = {'content-type':'application/json'})
        response  = self.app.get('/api/v1/parties')
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Returned successfully')
        self.assertEqual(response.status_code,200)


    def test_remove_party_usingid(self):
        self.app.post('/api/v1/parties',
                  data = json.dumps(self.test_party2),
                  headers = {'content-type':'application/json'})
        response = self.app.delete('/api/v1/parties/1')
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Party successfully deleted')
        self.assertEqual(response.status_code,200)


    def test_find_all_parties(self):
        response = self.app.get('/api/v1/parties')
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Returned successfully')
        self.assertEqual(response.status_code,200) 


    if __name__  ==  "__main__":
        unittest.main()
