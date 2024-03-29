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


class CreateBudgetBlueprintRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    
Blueprint for provisioning Budgets for a Budget Program.

    """


    class MetaOapg:
        required = {
            "limit_type",
            "spend_type",
            "limit",
            "limit_visibility",
            "period_type",
        }
        
        class properties:
        
            @staticmethod
            def period_type() -> typing.Type['PeriodType']:
                return PeriodType
        
            @staticmethod
            def limit() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def limit_type() -> typing.Type['LimitType']:
                return LimitType
        
            @staticmethod
            def spend_type() -> typing.Type['SpendType']:
                return SpendType
        
            @staticmethod
            def limit_visibility() -> typing.Type['BudgetLimitVisibilityType']:
                return BudgetLimitVisibilityType
            description = schemas.StrSchema
            name = schemas.StrSchema
            parent_budget_id = schemas.StrSchema
        
            @staticmethod
            def owner_user_ids() -> typing.Type['CreateBudgetBlueprintRequestOwnerUserIds']:
                return CreateBudgetBlueprintRequestOwnerUserIds
            
            
            class start_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'start_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class end_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'end_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "period_type": period_type,
                "limit": limit,
                "limit_type": limit_type,
                "spend_type": spend_type,
                "limit_visibility": limit_visibility,
                "description": description,
                "name": name,
                "parent_budget_id": parent_budget_id,
                "owner_user_ids": owner_user_ids,
                "start_date": start_date,
                "end_date": end_date,
            }
    
    limit_type: 'LimitType'
    spend_type: 'SpendType'
    limit: 'Money'
    limit_visibility: 'BudgetLimitVisibilityType'
    period_type: 'PeriodType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["period_type"]) -> 'PeriodType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit_type"]) -> 'LimitType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spend_type"]) -> 'SpendType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit_visibility"]) -> 'BudgetLimitVisibilityType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_budget_id"]) -> MetaOapg.properties.parent_budget_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_user_ids"]) -> 'CreateBudgetBlueprintRequestOwnerUserIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["period_type", "limit", "limit_type", "spend_type", "limit_visibility", "description", "name", "parent_budget_id", "owner_user_ids", "start_date", "end_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["period_type"]) -> 'PeriodType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> 'Money': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit_type"]) -> 'LimitType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spend_type"]) -> 'SpendType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit_visibility"]) -> 'BudgetLimitVisibilityType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_budget_id"]) -> typing.Union[MetaOapg.properties.parent_budget_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_user_ids"]) -> typing.Union['CreateBudgetBlueprintRequestOwnerUserIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["period_type", "limit", "limit_type", "spend_type", "limit_visibility", "description", "name", "parent_budget_id", "owner_user_ids", "start_date", "end_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        limit_type: 'LimitType',
        spend_type: 'SpendType',
        limit: 'Money',
        limit_visibility: 'BudgetLimitVisibilityType',
        period_type: 'PeriodType',
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        parent_budget_id: typing.Union[MetaOapg.properties.parent_budget_id, str, schemas.Unset] = schemas.unset,
        owner_user_ids: typing.Union['CreateBudgetBlueprintRequestOwnerUserIds', schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, None, str, date, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, None, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateBudgetBlueprintRequest':
        return super().__new__(
            cls,
            *args,
            limit_type=limit_type,
            spend_type=spend_type,
            limit=limit,
            limit_visibility=limit_visibility,
            period_type=period_type,
            description=description,
            name=name,
            parent_budget_id=parent_budget_id,
            owner_user_ids=owner_user_ids,
            start_date=start_date,
            end_date=end_date,
            _configuration=_configuration,
            **kwargs,
        )

from brex_budgets_python_sdk.model.budget_limit_visibility_type import BudgetLimitVisibilityType
from brex_budgets_python_sdk.model.create_budget_blueprint_request_owner_user_ids import CreateBudgetBlueprintRequestOwnerUserIds
from brex_budgets_python_sdk.model.limit_type import LimitType
from brex_budgets_python_sdk.model.money import Money
from brex_budgets_python_sdk.model.period_type import PeriodType
from brex_budgets_python_sdk.model.spend_type import SpendType
