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

from brex_budgets_python_sdk.pydantic.budget_blueprint import BudgetBlueprint
from brex_budgets_python_sdk.pydantic.budget_program_existing_budget_ids import BudgetProgramExistingBudgetIds
from brex_budgets_python_sdk.pydantic.budget_program_status import BudgetProgramStatus
from brex_budgets_python_sdk.pydantic.employee_filter import EmployeeFilter

class BudgetProgram(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    budget_blueprints: typing.List[BudgetBlueprint] = Field(alias='budget_blueprints')

    budget_program_status: BudgetProgramStatus = Field(alias='budget_program_status')

    created_at: date = Field(alias='created_at')

    updated_at: date = Field(alias='updated_at')

    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    existing_budget_ids: typing.Optional[BudgetProgramExistingBudgetIds] = Field(None, alias='existing_budget_ids')

    employee_filter: typing.Optional[EmployeeFilter] = Field(None, alias='employee_filter')

    creator_user_id: typing.Optional[typing.Optional[str]] = Field(None, alias='creator_user_id')
    class Config:
        arbitrary_types_allowed = True
