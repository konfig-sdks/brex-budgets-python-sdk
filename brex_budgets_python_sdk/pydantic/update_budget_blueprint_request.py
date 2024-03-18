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

from brex_budgets_python_sdk.pydantic.limit_type import LimitType
from brex_budgets_python_sdk.pydantic.money import Money
from brex_budgets_python_sdk.pydantic.period_type import PeriodType
from brex_budgets_python_sdk.pydantic.spend_type import SpendType
from brex_budgets_python_sdk.pydantic.update_budget_blueprint_request_owner_user_ids import UpdateBudgetBlueprintRequestOwnerUserIds

class UpdateBudgetBlueprintRequest(BaseModel):
    #  Description of what the Budget is used for. 
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    #  ID of budget blueprint to update, omit if adding new budget blueprint to budget program. 
    id: typing.Optional[typing.Optional[str]] = Field(None, alias='id')

    #  Name for the Budget. 
    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    #  ID of parent Budget. 
    parent_budget_id: typing.Optional[typing.Optional[str]] = Field(None, alias='parent_budget_id')

    owner_user_ids: typing.Optional[UpdateBudgetBlueprintRequestOwnerUserIds] = Field(None, alias='owner_user_ids')

    period_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='period_type')

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[typing.Optional[date]] = Field(None, alias='start_date')

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')

    limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit')

    limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit_type')

    spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='spend_type')
    class Config:
        arbitrary_types_allowed = True
