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

from brex_budgets_python_sdk.pydantic.budget_member_user_ids import BudgetMemberUserIds
from brex_budgets_python_sdk.pydantic.budget_owner_user_ids import BudgetOwnerUserIds
from brex_budgets_python_sdk.pydantic.budget_period_balance import BudgetPeriodBalance
from brex_budgets_python_sdk.pydantic.budget_status import BudgetStatus
from brex_budgets_python_sdk.pydantic.limit_type import LimitType
from brex_budgets_python_sdk.pydantic.money import Money
from brex_budgets_python_sdk.pydantic.period_type import PeriodType
from brex_budgets_python_sdk.pydantic.spend_type import SpendType

class Budget(BaseModel):
    period_type: PeriodType = Field(alias='period_type')

    budget_status: BudgetStatus = Field(alias='budget_status')

    spend_type: SpendType = Field(alias='spend_type')

    #  Description of what the Budget is used for. 
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    #  Unique ID for the Budget. 
    budget_id: typing.Optional[str] = Field(None, alias='budget_id')

    #  The Brex account this Budget belongs to. 
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    #  The ID of the user who originally created this budget. 
    creator_user_id: typing.Optional[typing.Optional[str]] = Field(None, alias='creator_user_id')

    #  Name for the Budget. 
    name: typing.Optional[str] = Field(None, alias='name')

    #  ID of parent Budget. 
    parent_budget_id: typing.Optional[typing.Optional[str]] = Field(None, alias='parent_budget_id')

    owner_user_ids: typing.Optional[BudgetOwnerUserIds] = Field(None, alias='owner_user_ids')

    member_user_ids: typing.Optional[BudgetMemberUserIds] = Field(None, alias='member_user_ids')

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[typing.Optional[date]] = Field(None, alias='start_date')

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')

    limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit')

    limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit_type')

    current_period_balance: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='current_period_balance')
    class Config:
        arbitrary_types_allowed = True
