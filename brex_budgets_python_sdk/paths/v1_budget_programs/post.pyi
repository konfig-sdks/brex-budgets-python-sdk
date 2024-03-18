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

from brex_budgets_python_sdk.model.create_budget_program_request import CreateBudgetProgramRequest as CreateBudgetProgramRequestSchema
from brex_budgets_python_sdk.model.employee_filter import EmployeeFilter as EmployeeFilterSchema
from brex_budgets_python_sdk.model.create_budget_blueprint_request import CreateBudgetBlueprintRequest as CreateBudgetBlueprintRequestSchema
from brex_budgets_python_sdk.model.budget_program import BudgetProgram as BudgetProgramSchema
from brex_budgets_python_sdk.model.create_budget_program_request_existing_budget_ids import CreateBudgetProgramRequestExistingBudgetIds as CreateBudgetProgramRequestExistingBudgetIdsSchema

from brex_budgets_python_sdk.type.employee_filter import EmployeeFilter
from brex_budgets_python_sdk.type.create_budget_blueprint_request import CreateBudgetBlueprintRequest
from brex_budgets_python_sdk.type.budget_program import BudgetProgram
from brex_budgets_python_sdk.type.create_budget_program_request_existing_budget_ids import CreateBudgetProgramRequestExistingBudgetIds
from brex_budgets_python_sdk.type.create_budget_program_request import CreateBudgetProgramRequest

from ...api_client import Dictionary
from brex_budgets_python_sdk.pydantic.create_budget_program_request import CreateBudgetProgramRequest as CreateBudgetProgramRequestPydantic
from brex_budgets_python_sdk.pydantic.create_budget_blueprint_request import CreateBudgetBlueprintRequest as CreateBudgetBlueprintRequestPydantic
from brex_budgets_python_sdk.pydantic.budget_program import BudgetProgram as BudgetProgramPydantic
from brex_budgets_python_sdk.pydantic.create_budget_program_request_existing_budget_ids import CreateBudgetProgramRequestExistingBudgetIds as CreateBudgetProgramRequestExistingBudgetIdsPydantic
from brex_budgets_python_sdk.pydantic.employee_filter import EmployeeFilter as EmployeeFilterPydantic

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
# body param
SchemaForRequestBodyApplicationJson = CreateBudgetProgramRequestSchema


request_body_create_budget_program_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = BudgetProgramSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: BudgetProgram


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: BudgetProgram


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_mapped_args(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if description is not None:
            _body["description"] = description
        if existing_budget_ids is not None:
            _body["existing_budget_ids"] = existing_budget_ids
        if budget_blueprints is not None:
            _body["budget_blueprints"] = budget_blueprints
        if employee_filter is not None:
            _body["employee_filter"] = employee_filter
        if name is not None:
            _body["name"] = name
        args.body = _body
        if idempotency_key is not None:
            _header_params["Idempotency-Key"] = idempotency_key
        args.header = _header_params
        return args

    async def _acreate_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
         Create Budget Program 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
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
            path_template='/v1/budget_programs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_budget_program_request.serialize(body, content_type)
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


    def _create_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
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
         Create Budget Program 
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
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
        method = 'post'.upper()
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
            path_template='/v1/budget_programs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_create_budget_program_request.serialize(body, content_type)
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


class CreateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            budget_blueprints=budget_blueprints,
            name=name,
            idempotency_key=idempotency_key,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
        )
        return await self._acreate_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def create(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            budget_blueprints=budget_blueprints,
            name=name,
            idempotency_key=idempotency_key,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
        )
        return self._create_oapg(
            body=args.body,
            header_params=args.header,
        )

class Create(BaseApi):

    async def acreate(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
        **kwargs,
    ) -> BudgetProgramPydantic:
        raw_response = await self.raw.acreate(
            budget_blueprints=budget_blueprints,
            name=name,
            idempotency_key=idempotency_key,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
            **kwargs,
        )
        if validate:
            return BudgetProgramPydantic(**raw_response.body)
        return api_client.construct_model_instance(BudgetProgramPydantic, raw_response.body)
    
    
    def create(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        validate: bool = False,
    ) -> BudgetProgramPydantic:
        raw_response = self.raw.create(
            budget_blueprints=budget_blueprints,
            name=name,
            idempotency_key=idempotency_key,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
        )
        if validate:
            return BudgetProgramPydantic(**raw_response.body)
        return api_client.construct_model_instance(BudgetProgramPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_mapped_args(
            budget_blueprints=budget_blueprints,
            name=name,
            idempotency_key=idempotency_key,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
        )
        return await self._acreate_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    def post(
        self,
        budget_blueprints: typing.List[CreateBudgetBlueprintRequest],
        name: str,
        idempotency_key: str,
        description: typing.Optional[typing.Optional[str]] = None,
        existing_budget_ids: typing.Optional[CreateBudgetProgramRequestExistingBudgetIds] = None,
        employee_filter: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_mapped_args(
            budget_blueprints=budget_blueprints,
            name=name,
            idempotency_key=idempotency_key,
            description=description,
            existing_budget_ids=existing_budget_ids,
            employee_filter=employee_filter,
        )
        return self._create_oapg(
            body=args.body,
            header_params=args.header,
        )

