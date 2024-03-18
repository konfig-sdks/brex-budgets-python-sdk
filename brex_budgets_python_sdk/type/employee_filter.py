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

from brex_budgets_python_sdk.type.employment_status import EmploymentStatus
from brex_budgets_python_sdk.type.employment_type import EmploymentType

class RequiredEmployeeFilter(TypedDict):
    pass

class OptionalEmployeeFilter(TypedDict, total=False):
    employment_status: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    employment_type: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class EmployeeFilter(RequiredEmployeeFilter, OptionalEmployeeFilter):
    pass
