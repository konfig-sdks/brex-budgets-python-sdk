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
from pydantic import BaseModel, Field, RootModel

from brex_budgets_python_sdk.pydantic.create_budget_blueprint_request import CreateBudgetBlueprintRequest
from brex_budgets_python_sdk.pydantic.create_budget_program_request_existing_budget_ids import CreateBudgetProgramRequestExistingBudgetIds
from brex_budgets_python_sdk.pydantic.employee_filter import EmployeeFilter

class CreateBudgetProgramRequest(BaseModel):
    budget_blueprints: typing.List[CreateBudgetBlueprintRequest] = Field(alias='budget_blueprints')

    name: str = Field(alias='name')

    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = Field(None, alias='existing_budget_ids')

    employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='employee_filter')
    class Config:
        arbitrary_types_allowed = True
