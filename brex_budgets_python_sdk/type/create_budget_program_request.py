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

from brex_budgets_python_sdk.type.create_budget_blueprint_request import CreateBudgetBlueprintRequest
from brex_budgets_python_sdk.type.create_budget_program_request_existing_budget_ids import CreateBudgetProgramRequestExistingBudgetIds
from brex_budgets_python_sdk.type.employee_filter import EmployeeFilter

class RequiredCreateBudgetProgramRequest(TypedDict):
    budget_blueprints: typing.List[CreateBudgetBlueprintRequest]

    name: str

class OptionalCreateBudgetProgramRequest(TypedDict, total=False):
    description: typing.Optional[str]

    existing_budget_ids: CreateBudgetProgramRequestExistingBudgetIds

    employee_filter: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class CreateBudgetProgramRequest(RequiredCreateBudgetProgramRequest, OptionalCreateBudgetProgramRequest):
    pass
