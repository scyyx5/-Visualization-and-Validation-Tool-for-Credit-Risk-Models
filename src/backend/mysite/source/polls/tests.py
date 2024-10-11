from urllib import response
from django.test import TestCase
from django.test import Client
import unittest
import json
import jsonschema
from jsonschema import validate
import psycopg2
import requests


userSchema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "user_fname": {"type": "string"},
        "user_lname": {"type": "string"},
        "user_email": {"type": "string"},
        "user_password": {"type": "string"},
    },
}



c = Client()

def validateMultipleJSON(jsonData, currentSchema):
    try:
        for json1 in jsonData:
            validate(instance=json1, schema=currentSchema)
    except jsonschema.exceptions.ValidationError as err: 
        return False 
    return True

def validateJSON(jsonData, currentSchema):
    try:
        validate(instance=jsonData, schema=currentSchema)
    except jsonschema.exceptions.ValidationError as err: 
        return False 
    return True

class userTestCase(TestCase):
    def test_log_in(self):
        response = requests.post("http://127.0.0.1:8000/api/v1/login/", json= {
        "email": "test@gmail.com",
        "password": "test123456"},
        verify=False)

        print(response.json())
        self.assertEqual(validateJSON(response.json(), userSchema), True)
        
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_invalid_user(self):

        response = c.post("/api/v1/login/", json= {"user_fname": "UNIQUETEXT23244411111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "user_lname": "UNIQUETEXT232444", "user_email": "UNIQUETEXT232444@gmail.com"})
        self.assertNotEqual(response.status_code, 200)

    def test_invalid_user2(self):

        response = c.post("/api/v1/login/", json= {    "username": "testaccount","password": "test1234"})
        self.assertNotEqual(response.status_code, 200)
        

    

    """
    def test_download_graph(self):
        #headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"}
        response = requests.get("http://127.0.0.1:8000/api/v1/download_graph/",
            headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"})
        #print(response.json())
        #self.assertEqual(validateJSON(response.json(), userSchema), True)

        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_dr_age_api(self):
        #headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"}
        response = requests.get("http://127.0.0.1:8000/api/v1/download_dr_age/",
            headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"})
        #print(response.json())
        #self.assertEqual(validateJSON(response.json(), userSchema), True)

        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    


    def test_dr_cal_api(self):
        #headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"}
        response = requests.get("http://127.0.0.1:8000/api/v1/download_dr_cal/",
            headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"})
        #print(response.json())
        #self.assertEqual(validateJSON(response.json(), userSchema), True)

        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    def test_lexis(self):
        #headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"}
        response = requests.get("http://127.0.0.1:8000/api/v1/download_lexis/",
            headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"})
        #print(response.json())
        #self.assertEqual(validateJSON(response.json(), userSchema), True)

        print(response.status_code)
        self.assertEqual(response.status_code, 200)


    def test_apc(self):
        #headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"}
        response = requests.get("http://127.0.0.1:8000/api/v1/download_apc/",
            headers = {"Authorization": "Token c83e4456ca2b14cd54ccbb96074169e7f46e34d8"})
        #print(response.json())
        #self.assertEqual(validateJSON(response.json(), userSchema), True)

        print(response.status_code)
        self.assertEqual(response.status_code, 200)
    """


suite = unittest.TestLoader().loadTestsFromTestCase(userTestCase)
unittest.TextTestRunner(verbosity=2).run(suite)