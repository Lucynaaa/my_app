import unittest
from hello_world import app

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_msg_with_output(self):
        response = self.app.get('/')
        self.assertEqual(b"Hello again Lucyna", response.data)
