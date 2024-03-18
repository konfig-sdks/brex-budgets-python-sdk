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

from brex_budgets_python_sdk.type.budget_blueprint_owner_user_ids import BudgetBlueprintOwnerUserIds
from brex_budgets_python_sdk.type.limit_type import LimitType
from brex_budgets_python_sdk.type.money import Money
from brex_budgets_python_sdk.type.period_type import PeriodType
from brex_budgets_python_sdk.type.spend_type import SpendType

class RequiredBudgetBlueprint(TypedDict):
    id: str

    period_type: PeriodType

    limit_type: LimitType

    spend_type: SpendType

class OptionalBudgetBlueprint(TypedDict, total=False):
    #  Description of what the Budget is used for. 
    description: typing.Optional[str]

    #  Name for the Budget. 
    name: str

    #  ID of parent Budget. 
    parent_budget_id: str

    owner_user_ids: BudgetBlueprintOwnerUserIds

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[date]

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[date]

    limit: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class BudgetBlueprint(RequiredBudgetBlueprint, OptionalBudgetBlueprint):
    pass
