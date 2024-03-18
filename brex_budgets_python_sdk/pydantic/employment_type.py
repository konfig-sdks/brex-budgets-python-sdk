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


EmploymentType = Literal["EMPLOYMENT_TYPE_FULL_TIME", "EMPLOYMENT_TYPE_PART_TIME", "EMPLOYMENT_TYPE_CONTRACTOR", "EMPLOYMENT_TYPE_INTERN", "EMPLOYMENT_TYPE_FREELANCE"]
