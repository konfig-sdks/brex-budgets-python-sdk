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
from brex_budgets_python_sdk.paths.v1_budget_programs_id import delete
from brex_budgets_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1BudgetProgramsId(ApiTestMixin, unittest.TestCase):
    """
    V1BudgetProgramsId unit test stubs
         Delete Budget Program 
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
