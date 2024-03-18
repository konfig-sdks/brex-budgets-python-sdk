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


class RequiredMoney(TypedDict):
    pass

class OptionalMoney(TypedDict, total=False):
    # The amount of money, in the smallest denomination of the currency indicated by currency. For example, when currency is USD, amount is in cents.
    amount: int

    # The type of currency, in ISO 4217 format. Default to USD if not specified
    currency: typing.Optional[str]

class Money(RequiredMoney, OptionalMoney):
    pass
