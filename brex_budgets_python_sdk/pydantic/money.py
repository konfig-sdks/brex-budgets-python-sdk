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


class Money(BaseModel):
    # The amount of money, in the smallest denomination of the currency indicated by currency. For example, when currency is USD, amount is in cents.
    amount: typing.Optional[int] = Field(None, alias='amount')

    # The type of currency, in ISO 4217 format. Default to USD if not specified
    currency: typing.Optional[typing.Optional[str]] = Field(None, alias='currency')
    class Config:
        arbitrary_types_allowed = True
