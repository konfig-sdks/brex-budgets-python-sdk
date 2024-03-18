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


class BudgetProgram(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    
Budget Program used to create budgets for eligible users.

    """


    class MetaOapg:
        required = {
            "updated_at",
            "name",
            "budget_blueprints",
            "created_at",
            "id",
            "budget_program_status",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class budget_blueprints(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BudgetBlueprint']:
                        return BudgetBlueprint
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BudgetBlueprint'], typing.List['BudgetBlueprint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'budget_blueprints':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BudgetBlueprint':
                    return super().__getitem__(i)
        
            @staticmethod
            def budget_program_status() -> typing.Type['BudgetProgramStatus']:
                return BudgetProgramStatus
            created_at = schemas.DateSchema
            updated_at = schemas.DateSchema
            
            
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
        
            @staticmethod
            def existing_budget_ids() -> typing.Type['BudgetProgramExistingBudgetIds']:
                return BudgetProgramExistingBudgetIds
        
            @staticmethod
            def employee_filter() -> typing.Type['EmployeeFilter']:
                return EmployeeFilter
            
            
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
            __annotations__ = {
                "id": id,
                "name": name,
                "budget_blueprints": budget_blueprints,
                "budget_program_status": budget_program_status,
                "created_at": created_at,
                "updated_at": updated_at,
                "description": description,
                "existing_budget_ids": existing_budget_ids,
                "employee_filter": employee_filter,
                "creator_user_id": creator_user_id,
            }
    
    updated_at: MetaOapg.properties.updated_at
    name: MetaOapg.properties.name
    budget_blueprints: MetaOapg.properties.budget_blueprints
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    budget_program_status: 'BudgetProgramStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budget_blueprints"]) -> MetaOapg.properties.budget_blueprints: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budget_program_status"]) -> 'BudgetProgramStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["existing_budget_ids"]) -> 'BudgetProgramExistingBudgetIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_filter"]) -> 'EmployeeFilter': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator_user_id"]) -> MetaOapg.properties.creator_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "budget_blueprints", "budget_program_status", "created_at", "updated_at", "description", "existing_budget_ids", "employee_filter", "creator_user_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budget_blueprints"]) -> MetaOapg.properties.budget_blueprints: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budget_program_status"]) -> 'BudgetProgramStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["existing_budget_ids"]) -> typing.Union['BudgetProgramExistingBudgetIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_filter"]) -> typing.Union['EmployeeFilter', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator_user_id"]) -> typing.Union[MetaOapg.properties.creator_user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "budget_blueprints", "budget_program_status", "created_at", "updated_at", "description", "existing_budget_ids", "employee_filter", "creator_user_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, date, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        budget_blueprints: typing.Union[MetaOapg.properties.budget_blueprints, list, tuple, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, date, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        budget_program_status: 'BudgetProgramStatus',
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        existing_budget_ids: typing.Union['BudgetProgramExistingBudgetIds', schemas.Unset] = schemas.unset,
        employee_filter: typing.Union['EmployeeFilter', schemas.Unset] = schemas.unset,
        creator_user_id: typing.Union[MetaOapg.properties.creator_user_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BudgetProgram':
        return super().__new__(
            cls,
            *args,
            updated_at=updated_at,
            name=name,
            budget_blueprints=budget_blueprints,
            created_at=created_at,
            id=id,
            budget_program_status=budget_program_status,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
            creator_user_id=creator_user_id,
            _configuration=_configuration,
            **kwargs,
        )

from brex_budgets_python_sdk.model.budget_blueprint import BudgetBlueprint
from brex_budgets_python_sdk.model.budget_program_existing_budget_ids import BudgetProgramExistingBudgetIds
from brex_budgets_python_sdk.model.budget_program_status import BudgetProgramStatus
from brex_budgets_python_sdk.model.employee_filter import EmployeeFilter