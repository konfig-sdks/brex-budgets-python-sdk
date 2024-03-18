# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from brex_budgets_python_sdk.type.employee_filter import EmployeeFilter
from brex_budgets_python_sdk.type.update_budget_blueprint_request import UpdateBudgetBlueprintRequest
from brex_budgets_python_sdk.type.update_budget_program_request_existing_budget_ids import UpdateBudgetProgramRequestExistingBudgetIds

class RequiredUpdateBudgetProgramRequest(TypedDict):
    pass

class OptionalUpdateBudgetProgramRequest(TypedDict, total=False):
    description: typing.Optional[str]

    existing_budget_ids: UpdateBudgetProgramRequestExistingBudgetIds

    #  The Blueprints to update the budget program with. Blueprints without an ID are treated as new blueprints to be created. Blueprints that exist currently on the Budget Program, but are missing from the input, will be deleted. 
    budget_blueprints: typing.Optional[typing.List[UpdateBudgetBlueprintRequest]]

    employee_filter: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    name: typing.Optional[str]

class UpdateBudgetProgramRequest(RequiredUpdateBudgetProgramRequest, OptionalUpdateBudgetProgramRequest):
    pass
