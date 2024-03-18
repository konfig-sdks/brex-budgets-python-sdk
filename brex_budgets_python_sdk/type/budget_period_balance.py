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

from brex_budgets_python_sdk.type.money import Money

class RequiredBudgetPeriodBalance(TypedDict):
    pass

class OptionalBudgetPeriodBalance(TypedDict, total=False):
    start_date: typing.Optional[date]

    end_date: typing.Optional[date]

    balance: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class BudgetPeriodBalance(RequiredBudgetPeriodBalance, OptionalBudgetPeriodBalance):
    pass
