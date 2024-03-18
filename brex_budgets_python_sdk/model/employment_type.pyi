# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from brex_budgets_python_sdk import schemas  # noqa: F401


class EmploymentType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    
What kind of employment the employee has.

    """
    
    @schemas.classproperty
    def FULL_TIME(cls):
        return cls("EMPLOYMENT_TYPE_FULL_TIME")
    
    @schemas.classproperty
    def PART_TIME(cls):
        return cls("EMPLOYMENT_TYPE_PART_TIME")
    
    @schemas.classproperty
    def CONTRACTOR(cls):
        return cls("EMPLOYMENT_TYPE_CONTRACTOR")
    
    @schemas.classproperty
    def INTERN(cls):
        return cls("EMPLOYMENT_TYPE_INTERN")
    
    @schemas.classproperty
    def FREELANCE(cls):
        return cls("EMPLOYMENT_TYPE_FREELANCE")