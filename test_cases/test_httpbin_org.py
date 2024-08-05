import sys
sys.path.append("C:\\Git\\")


import unittest
from api_testing.lib.request_lib import *

class Test(unittest.TestCase):

    def setUp(self):
        self.log_obj = Log()
        self.api_obj = API()
        self.logger = self.log_obj.log_module(__name__)
        self.url = "https://httpbin.org"

    def test_get_method(self):
        """
        Send /get request and validate response code
        """

        self.api = self.url + "/get"
        self.logger.info("Calling the get method")
        self.res = self.api_obj.get_method(self.api)
        self.assertEqual(self.res.status_code, 200)

    def test_post_method(self):
        """
        Send /post request with json body and validate response contains relevant data
        """
        self.api = self.url + "/post"
        self.payload = {
                        "name": "TestUser",
                        "id": 1
                       }
        self.response = self.api_obj.post_method(self.api,self.payload)
        self.assertEqual(self.response["json"]["name"], self.payload["name"])
        self.assertEqual(self.response["json"]["id"], self.payload["id"])

    def test_dynamic_data(self):








if __name__ == '__main__':
    unittest.main()



