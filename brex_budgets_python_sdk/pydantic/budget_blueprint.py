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

from brex_budgets_python_sdk.pydantic.budget_blueprint_owner_user_ids import BudgetBlueprintOwnerUserIds
from brex_budgets_python_sdk.pydantic.limit_type import LimitType
from brex_budgets_python_sdk.pydantic.money import Money
from brex_budgets_python_sdk.pydantic.period_type import PeriodType
from brex_budgets_python_sdk.pydantic.spend_type import SpendType

class BudgetBlueprint(BaseModel):
    id: str = Field(alias='id')

    period_type: PeriodType = Field(alias='period_type')

    limit_type: LimitType = Field(alias='limit_type')

    spend_type: SpendType = Field(alias='spend_type')

    #  Description of what the Budget is used for. 
    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    #  Name for the Budget. 
    name: typing.Optional[str] = Field(None, alias='name')

    #  ID of parent Budget. 
    parent_budget_id: typing.Optional[str] = Field(None, alias='parent_budget_id')

    owner_user_ids: typing.Optional[BudgetBlueprintOwnerUserIds] = Field(None, alias='owner_user_ids')

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[typing.Optional[date]] = Field(None, alias='start_date')

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')

    limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='limit')
    class Config:
        arbitrary_types_allowed = True
