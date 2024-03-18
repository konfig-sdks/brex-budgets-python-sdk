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


class Budget(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "spend_type",
            "budget_status",
            "period_type",
        }
        
        class properties:
        
            @staticmethod
            def period_type() -> typing.Type['PeriodType']:
                return PeriodType
        
            @staticmethod
            def budget_status() -> typing.Type['BudgetStatus']:
                return BudgetStatus
        
            @staticmethod
            def spend_type() -> typing.Type['SpendType']:
                return SpendType
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            budget_id = schemas.StrSchema
            account_id = schemas.StrSchema
            
            
            class creator_user_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'creator_user_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            name = schemas.StrSchema
            
            
            class parent_budget_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'parent_budget_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def owner_user_ids() -> typing.Type['BudgetOwnerUserIds']:
                return BudgetOwnerUserIds
        
            @staticmethod
            def member_user_ids() -> typing.Type['BudgetMemberUserIds']:
                return BudgetMemberUserIds
            
            
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
            
            
            class limit(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            Money,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'limit':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class limit_type(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            LimitType,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'limit_type':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class current_period_balance(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    all_of_1 = schemas.AnyTypeSchema
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            BudgetPeriodBalance,
                            cls.all_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'current_period_balance':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "period_type": period_type,
                "budget_status": budget_status,
                "spend_type": spend_type,
                "description": description,
                "budget_id": budget_id,
                "account_id": account_id,
                "creator_user_id": creator_user_id,
                "name": name,
                "parent_budget_id": parent_budget_id,
                "owner_user_ids": owner_user_ids,
                "member_user_ids": member_user_ids,
                "start_date": start_date,
                "end_date": end_date,
                "limit": limit,
                "limit_type": limit_type,
                "current_period_balance": current_period_balance,
            }
    
    spend_type: 'SpendType'
    budget_status: 'BudgetStatus'
    period_type: 'PeriodType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["period_type"]) -> 'PeriodType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budget_status"]) -> 'BudgetStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spend_type"]) -> 'SpendType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budget_id"]) -> MetaOapg.properties.budget_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator_user_id"]) -> MetaOapg.properties.creator_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_budget_id"]) -> MetaOapg.properties.parent_budget_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_user_ids"]) -> 'BudgetOwnerUserIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["member_user_ids"]) -> 'BudgetMemberUserIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit_type"]) -> MetaOapg.properties.limit_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_period_balance"]) -> MetaOapg.properties.current_period_balance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["period_type", "budget_status", "spend_type", "description", "budget_id", "account_id", "creator_user_id", "name", "parent_budget_id", "owner_user_ids", "member_user_ids", "start_date", "end_date", "limit", "limit_type", "current_period_balance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["period_type"]) -> 'PeriodType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budget_status"]) -> 'BudgetStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spend_type"]) -> 'SpendType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budget_id"]) -> typing.Union[MetaOapg.properties.budget_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator_user_id"]) -> typing.Union[MetaOapg.properties.creator_user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_budget_id"]) -> typing.Union[MetaOapg.properties.parent_budget_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_user_ids"]) -> typing.Union['BudgetOwnerUserIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["member_user_ids"]) -> typing.Union['BudgetMemberUserIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit_type"]) -> typing.Union[MetaOapg.properties.limit_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_period_balance"]) -> typing.Union[MetaOapg.properties.current_period_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["period_type", "budget_status", "spend_type", "description", "budget_id", "account_id", "creator_user_id", "name", "parent_budget_id", "owner_user_ids", "member_user_ids", "start_date", "end_date", "limit", "limit_type", "current_period_balance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        spend_type: 'SpendType',
        budget_status: 'BudgetStatus',
        period_type: 'PeriodType',
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        budget_id: typing.Union[MetaOapg.properties.budget_id, str, schemas.Unset] = schemas.unset,
        account_id: typing.Union[MetaOapg.properties.account_id, str, schemas.Unset] = schemas.unset,
        creator_user_id: typing.Union[MetaOapg.properties.creator_user_id, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        parent_budget_id: typing.Union[MetaOapg.properties.parent_budget_id, None, str, schemas.Unset] = schemas.unset,
        owner_user_ids: typing.Union['BudgetOwnerUserIds', schemas.Unset] = schemas.unset,
        member_user_ids: typing.Union['BudgetMemberUserIds', schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, None, str, date, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, None, str, date, schemas.Unset] = schemas.unset,
        limit: typing.Union[MetaOapg.properties.limit, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        limit_type: typing.Union[MetaOapg.properties.limit_type, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        current_period_balance: typing.Union[MetaOapg.properties.current_period_balance, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Budget':
        return super().__new__(
            cls,
            *args,
            spend_type=spend_type,
            budget_status=budget_status,
            period_type=period_type,
            description=description,
            budget_id=budget_id,
            account_id=account_id,
            creator_user_id=creator_user_id,
            name=name,
            parent_budget_id=parent_budget_id,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            limit_type=limit_type,
            current_period_balance=current_period_balance,
            _configuration=_configuration,
            **kwargs,
        )

from brex_budgets_python_sdk.model.budget_member_user_ids import BudgetMemberUserIds
from brex_budgets_python_sdk.model.budget_owner_user_ids import BudgetOwnerUserIds
from brex_budgets_python_sdk.model.budget_period_balance import BudgetPeriodBalance
from brex_budgets_python_sdk.model.budget_status import BudgetStatus
from brex_budgets_python_sdk.model.limit_type import LimitType
from brex_budgets_python_sdk.model.money import Money
from brex_budgets_python_sdk.model.period_type import PeriodType
from brex_budgets_python_sdk.model.spend_type import SpendType