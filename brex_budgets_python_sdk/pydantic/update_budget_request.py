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

from brex_budgets_python_sdk.pydantic.budget_limit_visibility_type import BudgetLimitVisibilityType
from brex_budgets_python_sdk.pydantic.limit_type import LimitType
from brex_budgets_python_sdk.pydantic.money import Money
from brex_budgets_python_sdk.pydantic.spend_type import SpendType
from brex_budgets_python_sdk.pydantic.update_budget_request_member_user_ids import UpdateBudgetRequestMemberUserIds
from brex_budgets_python_sdk.pydantic.update_budget_request_owner_user_ids import UpdateBudgetRequestOwnerUserIds

class UpdateBudgetRequest(BaseModel):
    #  Description of what the Budget is used for. 
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    #  Name for the Budget. 
    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = Field(None, alias='owner_user_ids')

    member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = Field(None, alias='member_user_ids')

    limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit')

    limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit_type')

    spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='spend_type')

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[typing.Optional[date]] = Field(None, alias='start_date')

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')

    limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit_visibility')
    class Config:
        arbitrary_types_allowed = True
