# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from brex_budgets_python_sdk.paths.v1_budget_programs.post import CreateRaw
from brex_budgets_python_sdk.paths.v1_budget_programs_id.get import GetByIdRaw
from brex_budgets_python_sdk.paths.v1_budget_programs.get import ListRaw
from brex_budgets_python_sdk.paths.v1_budget_programs_id.delete import RemoveProgramByIdRaw
from brex_budgets_python_sdk.paths.v1_budget_programs_id.put import UpdateProgramByIdRaw


class BudgetProgramsApiRaw(
    CreateRaw,
    GetByIdRaw,
    ListRaw,
    RemoveProgramByIdRaw,
    UpdateProgramByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
