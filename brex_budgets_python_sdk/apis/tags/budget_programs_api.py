# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from brex_budgets_python_sdk.paths.v1_budget_programs.post import Create
from brex_budgets_python_sdk.paths.v1_budget_programs_id.get import GetById
from brex_budgets_python_sdk.paths.v1_budget_programs.get import List
from brex_budgets_python_sdk.paths.v1_budget_programs_id.delete import RemoveProgramById
from brex_budgets_python_sdk.paths.v1_budget_programs_id.put import UpdateProgramById
from brex_budgets_python_sdk.apis.tags.budget_programs_api_raw import BudgetProgramsApiRaw


class BudgetProgramsApi(
    Create,
    GetById,
    List,
    RemoveProgramById,
    UpdateProgramById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BudgetProgramsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BudgetProgramsApiRaw(api_client)
