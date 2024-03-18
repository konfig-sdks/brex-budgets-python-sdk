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
from brex_budgets_python_sdk.pydantic.create_budget_request_member_user_ids import CreateBudgetRequestMemberUserIds
from brex_budgets_python_sdk.pydantic.create_budget_request_owner_user_ids import CreateBudgetRequestOwnerUserIds
from brex_budgets_python_sdk.pydantic.limit_type import LimitType
from brex_budgets_python_sdk.pydantic.money import Money
from brex_budgets_python_sdk.pydantic.period_type import PeriodType
from brex_budgets_python_sdk.pydantic.spend_type import SpendType

class CreateBudgetRequest(BaseModel):
    #  ID of parent Budget. 
    parent_budget_id: str = Field(alias='parent_budget_id')

    period_type: PeriodType = Field(alias='period_type')

    limit: Money = Field(alias='limit')

    limit_type: LimitType = Field(alias='limit_type')

    spend_type: SpendType = Field(alias='spend_type')

    limit_visibility: BudgetLimitVisibilityType = Field(alias='limit_visibility')

    #  Description of what the Budget is used for. 
    description: typing.Optional[str] = Field(None, alias='description')

    #  Name for the Budget. 
    name: typing.Optional[str] = Field(None, alias='name')

    owner_user_ids: typing.Optional[CreateBudgetRequestOwnerUserIds] = Field(None, alias='owner_user_ids')

    member_user_ids: typing.Optional[CreateBudgetRequestMemberUserIds] = Field(None, alias='member_user_ids')

    #  The UTC date when the Budget should start counting. 
    start_date: typing.Optional[typing.Optional[date]] = Field(None, alias='start_date')

    #  The UTC date when the Budget should stop counting. 
    end_date: typing.Optional[typing.Optional[date]] = Field(None, alias='end_date')
    class Config:
        arbitrary_types_allowed = True
