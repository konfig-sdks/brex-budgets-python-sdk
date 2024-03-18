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

from brex_budgets_python_sdk.type.budget import Budget

class RequiredPageBudget(TypedDict):
    items: typing.List[Budget]

class OptionalPageBudget(TypedDict, total=False):
    next_cursor: typing.Optional[str]

class PageBudget(RequiredPageBudget, OptionalPageBudget):
    pass
