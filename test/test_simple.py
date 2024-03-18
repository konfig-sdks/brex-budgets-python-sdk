# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import unittest

import os
from pprint import pprint
from brex_budgets_python_sdk import BrexBudgets

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        brexbudgets = BrexBudgets(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(brexbudgets)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
