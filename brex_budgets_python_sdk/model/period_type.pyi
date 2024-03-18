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


class PeriodType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    
Period type of the Budget e.g. MONTHLY.

    """
    
    @schemas.classproperty
    def WEEKLY(cls):
        return cls("WEEKLY")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("MONTHLY")
    
    @schemas.classproperty
    def QUARTERLY(cls):
        return cls("QUARTERLY")
    
    @schemas.classproperty
    def YEARLY(cls):
        return cls("YEARLY")
    
    @schemas.classproperty
    def ONE_TIME(cls):
        return cls("ONE_TIME")
