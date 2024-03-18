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

from brex_budgets_python_sdk.pydantic.employment_status import EmploymentStatus
from brex_budgets_python_sdk.pydantic.employment_type import EmploymentType

class EmployeeFilter(BaseModel):
    employment_status: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='employment_status')

    employment_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='employment_type')
    class Config:
        arbitrary_types_allowed = True
