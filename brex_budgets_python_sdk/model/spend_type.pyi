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


class SpendType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    
Whether this Budget only can be spent from by cards provisioned by this Budget. 

    """
    
    @schemas.classproperty
    def BUDGET_PROVISIONED_CARDS_ONLY(cls):
        return cls("BUDGET_PROVISIONED_CARDS_ONLY")
    
    @schemas.classproperty
    def NON_BUDGET_PROVISIONED_CARDS_ALLOWED(cls):
        return cls("NON_BUDGET_PROVISIONED_CARDS_ALLOWED")
