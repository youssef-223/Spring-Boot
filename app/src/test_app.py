import os
import unittest
from app import app

class GreetingTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['NAME'] = 'World'
        self.app = app.test_client()
        self.app.testing = True

    def test_default_greeting(self):
        response = self.app.get('/greeting')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, World!"})

    def test_custom_greeting(self):
        response = self.app.get('/greeting?name=Flask')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, Flask!"})

if __name__ == '_main_':
    unittest.main()