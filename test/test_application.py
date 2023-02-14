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

    def test_postSport(self):
        with application.test_client() as client:
            response = client.post("/sports",
                                   data=json.dumps({"name": "Football", "description": "descript"}),
                                   content_type='application/json'
                                   )
            assert response.status_code == 200

    def test_postSport_back(self):
        with application.test_client() as client:
            response = client.post("/backend/sports/",
                                   data=json.dumps({"idSport": [1, 2, 3, 4, 5, 6]}),
                                   content_type='application/json'
                                   )
            assert response.status_code == 200

    if __name__ == '__main__':
        unittest.main()
