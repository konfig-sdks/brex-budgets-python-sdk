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

from brex_budgets_python_sdk.pydantic.employee_filter import EmployeeFilter
from brex_budgets_python_sdk.pydantic.update_budget_blueprint_request import UpdateBudgetBlueprintRequest
from brex_budgets_python_sdk.pydantic.update_budget_program_request_existing_budget_ids import UpdateBudgetProgramRequestExistingBudgetIds

class UpdateBudgetProgramRequest(BaseModel):
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    existing_budget_ids: typing.Optional[UpdateBudgetProgramRequestExistingBudgetIds] = Field(None, alias='existing_budget_ids')

    #  The Blueprints to update the budget program with. Blueprints without an ID are treated as new blueprints to be created. Blueprints that exist currently on the Budget Program, but are missing from the input, will be deleted. 
    budget_blueprints: typing.Optional[typing.Optional[typing.List[UpdateBudgetBlueprintRequest]]] = Field(None, alias='budget_blueprints')

    employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='employee_filter')

    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')
    class Config:
        arbitrary_types_allowed = True
