# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.user_data import UserData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDevelopersController(BaseTestCase):
    """DevelopersController integration test stubs"""

    def test_train_model(self):
        """Test case for train_model

        Trains the static model.
        """
        trainData = [UserData()]
        query_string = [('newModelName', 'newModelName_example')]
        response = self.client.open(
            '/ben.wutzke/MachineLearningTest/1.0.0/train',
            method='POST',
            data=json.dumps(trainData),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
