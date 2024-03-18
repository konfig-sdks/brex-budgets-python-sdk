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

from brex_budgets_python_sdk.type.budget_member_user_ids import BudgetMemberUserIds
from brex_budgets_python_sdk.type.budget_owner_user_ids import BudgetOwnerUserIds
from brex_budgets_python_sdk.type.budget_period_balance import BudgetPeriodBalance
from brex_budgets_python_sdk.type.budget_status import BudgetStatus
from brex_budgets_python_sdk.type.limit_type import LimitType
from brex_budgets_python_sdk.type.money import Money
from brex_budgets_python_sdk.type.period_type import PeriodType
from brex_budgets_python_sdk.type.spend_type import SpendType

class RequiredBudget(TypedDict):
    period_type: PeriodType

    budget_status: BudgetStatus

    spend_type: SpendType

class OptionalBudget(TypedDict, total=False):
    #  Description of what the Budget is used for. 
    description: typing.Optional[str]

    #  Unique ID for the Budget. 
    budget_id: str

    #  The Brex account this Budget belongs to. 
    account_id: str

    #  The ID of the user who originally created this budget. 
    creator_user_id: typing.Optional[str]

    #  Name for the Budget. 
    name: str

    #  ID of parent Budget. 
    parent_budget_id: typing.Optional[str]

    owner_user_ids: BudgetOwnerUserIds

    member_user_ids: BudgetMemberUserIds

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[date]

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[date]

    limit: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    limit_type: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    current_period_balance: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Budget(RequiredBudget, OptionalBudget):
    pass
