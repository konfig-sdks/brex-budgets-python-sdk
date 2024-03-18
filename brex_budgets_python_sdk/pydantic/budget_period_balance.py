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

from brex_budgets_python_sdk.pydantic.money import Money

class BudgetPeriodBalance(BaseModel):
    start_date: typing.Optional[typing.Optional[date]] = Field(None, alias='start_date')

    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')

    balance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='balance')
    class Config:
        arbitrary_types_allowed = True
