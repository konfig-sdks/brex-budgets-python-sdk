# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest
from unittest.mock import patch

import urllib3

import brex_budgets_python_sdk
from brex_budgets_python_sdk.paths.v1_budgets_id_archive import post
from brex_budgets_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1BudgetsIdArchive(ApiTestMixin, unittest.TestCase):
    """
    V1BudgetsIdArchive unit test stubs
         Archive a budget 
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
