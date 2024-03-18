# coding: utf-8
"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

import typing
import inspect
from datetime import date, datetime
from brex_budgets_python_sdk.client_custom import ClientCustom
from brex_budgets_python_sdk.configuration import Configuration
from brex_budgets_python_sdk.api_client import ApiClient
from brex_budgets_python_sdk.type_util import copy_signature
from brex_budgets_python_sdk.apis.tags.budget_programs_api import BudgetProgramsApi
from brex_budgets_python_sdk.apis.tags.budgets_api import BudgetsApi



class BrexBudgets(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.budget_programs: BudgetProgramsApi = BudgetProgramsApi(api_client)
        self.budgets: BudgetsApi = BudgetsApi(api_client)
