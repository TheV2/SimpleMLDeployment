# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user_data import UserData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_predict_model(self):
        """Test case for predict_model

        Takes input data from user and runs model for prediction.
        """
        predictData = [UserData()]
        query_string = [('modelName', 'modelName_example')]
        response = self.client.open(
            '/ben.wutzke/MachineLearningTest/1.0.0/predict',
            method='GET',
            data=json.dumps(predictData),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
