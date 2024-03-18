<div align="left">

[![Visit Brex](./header.png)](https://brex.com)

# Brex<a id="brex"></a>


The budgets API lets you manage your Brex budgets.



</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`brexbudgets.budget_programs.create`](#brexbudgetsbudget_programscreate)
  * [`brexbudgets.budget_programs.get_by_id`](#brexbudgetsbudget_programsget_by_id)
  * [`brexbudgets.budget_programs.list`](#brexbudgetsbudget_programslist)
  * [`brexbudgets.budget_programs.remove_program_by_id`](#brexbudgetsbudget_programsremove_program_by_id)
  * [`brexbudgets.budget_programs.update_program_by_id`](#brexbudgetsbudget_programsupdate_program_by_id)
  * [`brexbudgets.budgets.archive_budget_by_id`](#brexbudgetsbudgetsarchive_budget_by_id)
  * [`brexbudgets.budgets.create`](#brexbudgetsbudgetscreate)
  * [`brexbudgets.budgets.get_by_id`](#brexbudgetsbudgetsget_by_id)
  * [`brexbudgets.budgets.list`](#brexbudgetsbudgetslist)
  * [`brexbudgets.budgets.update_budget`](#brexbudgetsbudgetsupdate_budget)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Brex&serviceName=Budgets&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from brex_budgets_python_sdk import BrexBudgets, ApiException

brexbudgets = BrexBudgets(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    #  Create Budget Program
    create_response = brexbudgets.budget_programs.create(
        budget_blueprints=[
            {
                "period_type": "WEEKLY",
                "limit": {},
                "limit_type": "HARD",
                "spend_type": "BUDGET_PROVISIONED_CARDS_ONLY",
                "limit_visibility": "SHARED",
            }
        ],
        name="string_example",
        idempotency_key="Idempotency-Key_example",
        description="string_example",
        existing_budget_ids=["string_example"],
        employee_filter=None,
    )
    print(create_response)
except ApiException as e:
    print("Exception when calling BudgetProgramsApi.create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from brex_budgets_python_sdk import BrexBudgets, ApiException

brexbudgets = BrexBudgets(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        #  Create Budget Program
        create_response = await brexbudgets.budget_programs.acreate(
            budget_blueprints=[
                {
                    "period_type": "WEEKLY",
                    "limit": {},
                    "limit_type": "HARD",
                    "spend_type": "BUDGET_PROVISIONED_CARDS_ONLY",
                    "limit_visibility": "SHARED",
                }
            ],
            name="string_example",
            idempotency_key="Idempotency-Key_example",
            description="string_example",
            existing_budget_ids=["string_example"],
            employee_filter=None,
        )
        print(create_response)
    except ApiException as e:
        print("Exception when calling BudgetProgramsApi.create: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from brex_budgets_python_sdk import BrexBudgets, ApiException

brexbudgets = BrexBudgets(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    #  Create Budget Program
    create_response = brexbudgets.budget_programs.raw.create(
        budget_blueprints=[
            {
                "period_type": "WEEKLY",
                "limit": {},
                "limit_type": "HARD",
                "spend_type": "BUDGET_PROVISIONED_CARDS_ONLY",
                "limit_visibility": "SHARED",
            }
        ],
        name="string_example",
        idempotency_key="Idempotency-Key_example",
        description="string_example",
        existing_budget_ids=["string_example"],
        employee_filter=None,
    )
    pprint(create_response.body)
    pprint(create_response.body["id"])
    pprint(create_response.body["name"])
    pprint(create_response.body["budget_blueprints"])
    pprint(create_response.body["budget_program_status"])
    pprint(create_response.body["created_at"])
    pprint(create_response.body["updated_at"])
    pprint(create_response.body["description"])
    pprint(create_response.body["existing_budget_ids"])
    pprint(create_response.body["employee_filter"])
    pprint(create_response.body["creator_user_id"])
    pprint(create_response.headers)
    pprint(create_response.status)
    pprint(create_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BudgetProgramsApi.create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `brexbudgets.budget_programs.create`<a id="brexbudgetsbudget_programscreate"></a>


Creates a Budget Program.
If your account does not have access to budget program features, a 403 response status will be returned.
If this is the case and you want to gain access to this endpoint, please contact Brex support.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = brexbudgets.budget_programs.create(
    budget_blueprints=[
        {
            "period_type": "WEEKLY",
            "limit": {},
            "limit_type": "HARD",
            "spend_type": "BUDGET_PROVISIONED_CARDS_ONLY",
            "limit_visibility": "SHARED",
        }
    ],
    name="string_example",
    idempotency_key="Idempotency-Key_example",
    description="string_example",
    existing_budget_ids=["string_example"],
    employee_filter=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### budget_blueprints: List[`CreateBudgetBlueprintRequest`]<a id="budget_blueprints-listcreatebudgetblueprintrequest"></a>

##### name: `str`<a id="name-str"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### existing_budget_ids: [`CreateBudgetProgramRequestExistingBudgetIds`](./brex_budgets_python_sdk/type/create_budget_program_request_existing_budget_ids.py)<a id="existing_budget_ids-createbudgetprogramrequestexistingbudgetidsbrex_budgets_python_sdktypecreate_budget_program_request_existing_budget_idspy"></a>

##### employee_filter: Union[`EmployeeFilter`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_budgets_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="employee_filter-unionemployeefilter-unionbool-date-datetime-dict-float-int-list-str-nonebrex_budgets_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateBudgetProgramRequest`](./brex_budgets_python_sdk/type/create_budget_program_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BudgetProgram`](./brex_budgets_python_sdk/pydantic/budget_program.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budget_programs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budget_programs.get_by_id`<a id="brexbudgetsbudget_programsget_by_id"></a>


Retrieves a Budget Program by ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = brexbudgets.budget_programs.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetProgram`](./brex_budgets_python_sdk/pydantic/budget_program.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budget_programs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budget_programs.list`<a id="brexbudgetsbudget_programslist"></a>


Lists Budget Programs belonging to this account


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = brexbudgets.budget_programs.list(
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageBudgetProgram`](./brex_budgets_python_sdk/pydantic/page_budget_program.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budget_programs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budget_programs.remove_program_by_id`<a id="brexbudgetsbudget_programsremove_program_by_id"></a>


Delete a Budget Program by ID.
This endpoint requires budget management. If your account does not have access to budget management features, a 403 response status will be returned. 
If this is the case and you want to gain access to this endpoint, please contact Brex support.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_program_by_id_response = brexbudgets.budget_programs.remove_program_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BudgetProgram`](./brex_budgets_python_sdk/pydantic/budget_program.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budget_programs/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budget_programs.update_program_by_id`<a id="brexbudgetsbudget_programsupdate_program_by_id"></a>


Updates a Budget Program.
This endpoint requires budget management. If your account does not have access to budget management features, a 403 response status will be returned. 
If this is the case and you want to gain access to this endpoint, please contact Brex support.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_program_by_id_response = brexbudgets.budget_programs.update_program_by_id(
    id="id_example",
    idempotency_key="Idempotency-Key_example",
    description="string_example",
    existing_budget_ids=["string_example"],
    budget_blueprints=[{}],
    employee_filter=None,
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### existing_budget_ids: [`UpdateBudgetProgramRequestExistingBudgetIds`](./brex_budgets_python_sdk/type/update_budget_program_request_existing_budget_ids.py)<a id="existing_budget_ids-updatebudgetprogramrequestexistingbudgetidsbrex_budgets_python_sdktypeupdate_budget_program_request_existing_budget_idspy"></a>

##### budget_blueprints: List[`UpdateBudgetBlueprintRequest`]<a id="budget_blueprints-listupdatebudgetblueprintrequest"></a>

 The Blueprints to update the budget program with. Blueprints without an ID are treated as new blueprints to be created. Blueprints that exist currently on the Budget Program, but are missing from the input, will be deleted. 

##### employee_filter: Union[`EmployeeFilter`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_budgets_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="employee_filter-unionemployeefilter-unionbool-date-datetime-dict-float-int-list-str-nonebrex_budgets_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### name: `Optional[str]`<a id="name-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateBudgetProgramRequest`](./brex_budgets_python_sdk/type/update_budget_program_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BudgetProgram`](./brex_budgets_python_sdk/pydantic/budget_program.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budget_programs/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budgets.archive_budget_by_id`<a id="brexbudgetsbudgetsarchive_budget_by_id"></a>


Archives a budget, making it unusable for future expenses and removing it from the UI


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
brexbudgets.budgets.archive_budget_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budgets/{id}/archive` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budgets.create`<a id="brexbudgetsbudgetscreate"></a>


Creates a Budget.
This endpoint requires budget management. If your account does not have access to budget management features, a 403 response status will be returned. 
If this is the case and you want to gain access to this endpoint, please contact Brex support.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = brexbudgets.budgets.create(
    parent_budget_id="string_example",
    period_type="WEEKLY",
    limit={},
    limit_type="HARD",
    spend_type="BUDGET_PROVISIONED_CARDS_ONLY",
    limit_visibility="SHARED",
    idempotency_key="Idempotency-Key_example",
    description="string_example",
    name="string_example",
    owner_user_ids=["string_example"],
    member_user_ids=["string_example"],
    start_date="1970-01-01",
    end_date="1970-01-01",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### parent_budget_id: `str`<a id="parent_budget_id-str"></a>

 ID of parent Budget. 

##### period_type: [`PeriodType`](./brex_budgets_python_sdk/type/period_type.py)<a id="period_type-periodtypebrex_budgets_python_sdktypeperiod_typepy"></a>

##### limit: [`Money`](./brex_budgets_python_sdk/type/money.py)<a id="limit-moneybrex_budgets_python_sdktypemoneypy"></a>


##### limit_type: [`LimitType`](./brex_budgets_python_sdk/type/limit_type.py)<a id="limit_type-limittypebrex_budgets_python_sdktypelimit_typepy"></a>

##### spend_type: [`SpendType`](./brex_budgets_python_sdk/type/spend_type.py)<a id="spend_type-spendtypebrex_budgets_python_sdktypespend_typepy"></a>

##### limit_visibility: [`BudgetLimitVisibilityType`](./brex_budgets_python_sdk/type/budget_limit_visibility_type.py)<a id="limit_visibility-budgetlimitvisibilitytypebrex_budgets_python_sdktypebudget_limit_visibility_typepy"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

##### description: `str`<a id="description-str"></a>

 Description of what the Budget is used for. 

##### name: `str`<a id="name-str"></a>

 Name for the Budget. 

##### owner_user_ids: [`CreateBudgetRequestOwnerUserIds`](./brex_budgets_python_sdk/type/create_budget_request_owner_user_ids.py)<a id="owner_user_ids-createbudgetrequestowneruseridsbrex_budgets_python_sdktypecreate_budget_request_owner_user_idspy"></a>

##### member_user_ids: [`CreateBudgetRequestMemberUserIds`](./brex_budgets_python_sdk/type/create_budget_request_member_user_ids.py)<a id="member_user_ids-createbudgetrequestmemberuseridsbrex_budgets_python_sdktypecreate_budget_request_member_user_idspy"></a>

##### start_date: `Optional[date]`<a id="start_date-optionaldate"></a>

 The UTC date when the Budget should start counting. 

##### end_date: `Optional[date]`<a id="end_date-optionaldate"></a>

 The UTC date when the Budget should stop counting. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateBudgetRequest`](./brex_budgets_python_sdk/type/create_budget_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Budget`](./brex_budgets_python_sdk/pydantic/budget.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budgets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budgets.get_by_id`<a id="brexbudgetsbudgetsget_by_id"></a>


Retrieves a Budget by ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = brexbudgets.budgets.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Budget`](./brex_budgets_python_sdk/pydantic/budget.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budgets/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budgets.list`<a id="brexbudgetsbudgetslist"></a>


Lists Budgets belonging to this account


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = brexbudgets.budgets.list(
    cursor="string_example",
    limit=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### cursor: `Optional[str]`<a id="cursor-optionalstr"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`PageBudget`](./brex_budgets_python_sdk/pydantic/page_budget.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budgets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `brexbudgets.budgets.update_budget`<a id="brexbudgetsbudgetsupdate_budget"></a>


Updates a Budget.
This endpoint requires budget management. If your account does not have access to budget management features, a 403 response status will be returned. 
If this is the case and you want to gain access to this endpoint, please contact Brex support.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_budget_response = brexbudgets.budgets.update_budget(
    id="id_example",
    idempotency_key="Idempotency-Key_example",
    description="string_example",
    name="string_example",
    owner_user_ids=["string_example"],
    member_user_ids=["string_example"],
    limit=None,
    limit_type=None,
    spend_type=None,
    start_date="1970-01-01",
    end_date="1970-01-01",
    limit_visibility=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

 Description of what the Budget is used for. 

##### name: `Optional[str]`<a id="name-optionalstr"></a>

 Name for the Budget. 

##### owner_user_ids: [`UpdateBudgetRequestOwnerUserIds`](./brex_budgets_python_sdk/type/update_budget_request_owner_user_ids.py)<a id="owner_user_ids-updatebudgetrequestowneruseridsbrex_budgets_python_sdktypeupdate_budget_request_owner_user_idspy"></a>

##### member_user_ids: [`UpdateBudgetRequestMemberUserIds`](./brex_budgets_python_sdk/type/update_budget_request_member_user_ids.py)<a id="member_user_ids-updatebudgetrequestmemberuseridsbrex_budgets_python_sdktypeupdate_budget_request_member_user_idspy"></a>

##### limit: Union[`Money`, [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_budgets_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="limit-unionmoney-unionbool-date-datetime-dict-float-int-list-str-nonebrex_budgets_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### limit_type: Union[[`LimitType`](./brex_budgets_python_sdk/type/limit_type.py), [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_budgets_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="limit_type-unionlimittypebrex_budgets_python_sdktypelimit_typepy-unionbool-date-datetime-dict-float-int-list-str-nonebrex_budgets_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### spend_type: Union[[`SpendType`](./brex_budgets_python_sdk/type/spend_type.py), [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_budgets_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="spend_type-unionspendtypebrex_budgets_python_sdktypespend_typepy-unionbool-date-datetime-dict-float-int-list-str-nonebrex_budgets_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


##### start_date: `Optional[date]`<a id="start_date-optionaldate"></a>

 The UTC date when the Budget should start counting. 

##### end_date: `Optional[date]`<a id="end_date-optionaldate"></a>

 The UTC date when the Budget should stop counting. 

##### limit_visibility: Union[[`BudgetLimitVisibilityType`](./brex_budgets_python_sdk/type/budget_limit_visibility_type.py), [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./brex_budgets_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)]<a id="limit_visibility-unionbudgetlimitvisibilitytypebrex_budgets_python_sdktypebudget_limit_visibility_typepy-unionbool-date-datetime-dict-float-int-list-str-nonebrex_budgets_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateBudgetRequest`](./brex_budgets_python_sdk/type/update_budget_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Budget`](./brex_budgets_python_sdk/pydantic/budget.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/budgets/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
