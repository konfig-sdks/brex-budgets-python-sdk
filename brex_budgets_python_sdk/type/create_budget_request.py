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

from brex_budgets_python_sdk.type.budget_limit_visibility_type import BudgetLimitVisibilityType
from brex_budgets_python_sdk.type.create_budget_request_member_user_ids import CreateBudgetRequestMemberUserIds
from brex_budgets_python_sdk.type.create_budget_request_owner_user_ids import CreateBudgetRequestOwnerUserIds
from brex_budgets_python_sdk.type.limit_type import LimitType
from brex_budgets_python_sdk.type.money import Money
from brex_budgets_python_sdk.type.period_type import PeriodType
from brex_budgets_python_sdk.type.spend_type import SpendType

class RequiredCreateBudgetRequest(TypedDict):
    #  ID of parent Budget. 
    parent_budget_id: str

    period_type: PeriodType

    limit: Money

    limit_type: LimitType

    spend_type: SpendType

    limit_visibility: BudgetLimitVisibilityType

class OptionalCreateBudgetRequest(TypedDict, total=False):
    #  Description of what the Budget is used for. 
    description: str

    #  Name for the Budget. 
    name: str

    owner_user_ids: CreateBudgetRequestOwnerUserIds

    member_user_ids: CreateBudgetRequestMemberUserIds

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[date]

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[date]

class CreateBudgetRequest(RequiredCreateBudgetRequest, OptionalCreateBudgetRequest):
    pass
