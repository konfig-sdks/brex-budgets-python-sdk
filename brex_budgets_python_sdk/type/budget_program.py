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

from brex_budgets_python_sdk.type.budget_blueprint import BudgetBlueprint
from brex_budgets_python_sdk.type.budget_program_existing_budget_ids import BudgetProgramExistingBudgetIds
from brex_budgets_python_sdk.type.budget_program_status import BudgetProgramStatus
from brex_budgets_python_sdk.type.employee_filter import EmployeeFilter

class RequiredBudgetProgram(TypedDict):
    id: str

    name: str

    budget_blueprints: typing.List[BudgetBlueprint]

    budget_program_status: BudgetProgramStatus

    created_at: date

    updated_at: date

class OptionalBudgetProgram(TypedDict, total=False):
    description: typing.Optional[str]

    existing_budget_ids: BudgetProgramExistingBudgetIds

    employee_filter: EmployeeFilter

    creator_user_id: typing.Optional[str]

class BudgetProgram(RequiredBudgetProgram, OptionalBudgetProgram):
    pass
