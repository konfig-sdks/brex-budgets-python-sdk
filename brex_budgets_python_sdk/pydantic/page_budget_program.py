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

from brex_budgets_python_sdk.pydantic.budget_program import BudgetProgram

class PageBudgetProgram(BaseModel):
    items: typing.List[BudgetProgram] = Field(alias='items')

    next_cursor: typing.Optional[typing.Optional[str]] = Field(None, alias='next_cursor')
    class Config:
        arbitrary_types_allowed = True
