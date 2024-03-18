# coding: utf-8

"""
    Budgets API

     The budgets API lets you manage your Brex budgets. 

    The version of the OpenAPI document: 1.0
    Contact: developer-access@brex.com
    Created by: https://brex.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from brex_budgets_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from brex_budgets_python_sdk.api_response import AsyncGeneratorResponse
from brex_budgets_python_sdk import api_client, exceptions
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

from brex_budgets_python_sdk.model.budget import Budget as BudgetSchema
from brex_budgets_python_sdk.model.budget_limit_visibility_type import BudgetLimitVisibilityType as BudgetLimitVisibilityTypeSchema
from brex_budgets_python_sdk.model.update_budget_request import UpdateBudgetRequest as UpdateBudgetRequestSchema
from brex_budgets_python_sdk.model.update_budget_request_owner_user_ids import UpdateBudgetRequestOwnerUserIds as UpdateBudgetRequestOwnerUserIdsSchema
from brex_budgets_python_sdk.model.update_budget_request_member_user_ids import UpdateBudgetRequestMemberUserIds as UpdateBudgetRequestMemberUserIdsSchema
from brex_budgets_python_sdk.model.spend_type import SpendType as SpendTypeSchema
from brex_budgets_python_sdk.model.limit_type import LimitType as LimitTypeSchema
from brex_budgets_python_sdk.model.money import Money as MoneySchema

from brex_budgets_python_sdk.type.limit_type import LimitType
from brex_budgets_python_sdk.type.update_budget_request_member_user_ids import UpdateBudgetRequestMemberUserIds
from brex_budgets_python_sdk.type.budget_limit_visibility_type import BudgetLimitVisibilityType
from brex_budgets_python_sdk.type.update_budget_request_owner_user_ids import UpdateBudgetRequestOwnerUserIds
from brex_budgets_python_sdk.type.spend_type import SpendType
from brex_budgets_python_sdk.type.money import Money
from brex_budgets_python_sdk.type.budget import Budget
from brex_budgets_python_sdk.type.update_budget_request import UpdateBudgetRequest

from ...api_client import Dictionary
from brex_budgets_python_sdk.pydantic.money import Money as MoneyPydantic
from brex_budgets_python_sdk.pydantic.update_budget_request_owner_user_ids import UpdateBudgetRequestOwnerUserIds as UpdateBudgetRequestOwnerUserIdsPydantic
from brex_budgets_python_sdk.pydantic.budget_limit_visibility_type import BudgetLimitVisibilityType as BudgetLimitVisibilityTypePydantic
from brex_budgets_python_sdk.pydantic.spend_type import SpendType as SpendTypePydantic
from brex_budgets_python_sdk.pydantic.budget import Budget as BudgetPydantic
from brex_budgets_python_sdk.pydantic.limit_type import LimitType as LimitTypePydantic
from brex_budgets_python_sdk.pydantic.update_budget_request import UpdateBudgetRequest as UpdateBudgetRequestPydantic
from brex_budgets_python_sdk.pydantic.update_budget_request_member_user_ids import UpdateBudgetRequestMemberUserIds as UpdateBudgetRequestMemberUserIdsPydantic

# Header params
IdempotencyKeySchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'Idempotency-Key': typing.Union[IdempotencyKeySchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_idempotency_key = api_client.HeaderParameter(
    name="Idempotency-Key",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdempotencyKeySchema,
    required=True,
)
# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UpdateBudgetRequestSchema


request_body_update_budget_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = BudgetSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Budget


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Budget


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _update_budget_mapped_args(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if owner_user_ids is not None:
            _body["owner_user_ids"] = owner_user_ids
        if member_user_ids is not None:
            _body["member_user_ids"] = member_user_ids
        if limit is not None:
            _body["limit"] = limit
        if limit_type is not None:
            _body["limit_type"] = limit_type
        if spend_type is not None:
            _body["spend_type"] = spend_type
        if start_date is not None:
            _body["start_date"] = start_date
        if end_date is not None:
            _body["end_date"] = end_date
        if limit_visibility is not None:
            _body["limit_visibility"] = limit_visibility
        args.body = _body
        if idempotency_key is not None:
            _header_params["Idempotency-Key"] = idempotency_key
        if id is not None:
            _path_params["id"] = id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _aupdate_budget_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
         Update Budget 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_idempotency_key,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/budgets/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_budget_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _update_budget_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
         Update Budget 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_idempotency_key,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/budgets/{id}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_update_budget_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class UpdateBudgetRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_budget(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_budget_mapped_args(
            id=id,
            idempotency_key=idempotency_key,
            description=description,
            name=name,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            limit=limit,
            limit_type=limit_type,
            spend_type=spend_type,
            start_date=start_date,
            end_date=end_date,
            limit_visibility=limit_visibility,
        )
        return await self._aupdate_budget_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def update_budget(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_budget_mapped_args(
            id=id,
            idempotency_key=idempotency_key,
            description=description,
            name=name,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            limit=limit,
            limit_type=limit_type,
            spend_type=spend_type,
            start_date=start_date,
            end_date=end_date,
            limit_visibility=limit_visibility,
        )
        return self._update_budget_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class UpdateBudget(BaseApi):

    async def aupdate_budget(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
        **kwargs,
    ) -> BudgetPydantic:
        raw_response = await self.raw.aupdate_budget(
            id=id,
            idempotency_key=idempotency_key,
            description=description,
            name=name,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            limit=limit,
            limit_type=limit_type,
            spend_type=spend_type,
            start_date=start_date,
            end_date=end_date,
            limit_visibility=limit_visibility,
            **kwargs,
        )
        if validate:
            return BudgetPydantic(**raw_response.body)
        return api_client.construct_model_instance(BudgetPydantic, raw_response.body)
    
    
    def update_budget(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
    ) -> BudgetPydantic:
        raw_response = self.raw.update_budget(
            id=id,
            idempotency_key=idempotency_key,
            description=description,
            name=name,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            limit=limit,
            limit_type=limit_type,
            spend_type=spend_type,
            start_date=start_date,
            end_date=end_date,
            limit_visibility=limit_visibility,
        )
        if validate:
            return BudgetPydantic(**raw_response.body)
        return api_client.construct_model_instance(BudgetPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_budget_mapped_args(
            id=id,
            idempotency_key=idempotency_key,
            description=description,
            name=name,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            limit=limit,
            limit_type=limit_type,
            spend_type=spend_type,
            start_date=start_date,
            end_date=end_date,
            limit_visibility=limit_visibility,
        )
        return await self._aupdate_budget_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        id: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        name: typing.Optional[typing.Optional[str]] = None,
        owner_user_ids: typing.Optional[UpdateBudgetRequestOwnerUserIds] = None,
        member_user_ids: typing.Optional[UpdateBudgetRequestMemberUserIds] = None,
        limit: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        limit_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        spend_type: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        start_date: typing.Optional[typing.Optional[date]] = None,
        end_date: typing.Optional[typing.Optional[date]] = None,
        limit_visibility: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_budget_mapped_args(
            id=id,
            idempotency_key=idempotency_key,
            description=description,
            name=name,
            owner_user_ids=owner_user_ids,
            member_user_ids=member_user_ids,
            limit=limit,
            limit_type=limit_type,
            spend_type=spend_type,
            start_date=start_date,
            end_date=end_date,
            limit_visibility=limit_visibility,
        )
        return self._update_budget_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

