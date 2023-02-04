import json
import unittest

import application
from application import *


class ViewTest(unittest.TestCase):
    unittest.TestLoader.sortTestMethodsUsing = None

    def test_getSport(self):
        with application.test_client() as client:
            response = client.get("/sports")
            statusCode = response.status_code
            self.assertEqual(statusCode, 200)

    if __name__ == '__main__':
        unittest.main()
