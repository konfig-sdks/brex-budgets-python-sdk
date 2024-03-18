# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from brex_budgets_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_BUDGET_PROGRAMS = "/v1/budget_programs"
    V1_BUDGET_PROGRAMS_ID = "/v1/budget_programs/{id}"
    V1_BUDGETS = "/v1/budgets"
    V1_BUDGETS_ID = "/v1/budgets/{id}"
    V1_BUDGETS_ID_ARCHIVE = "/v1/budgets/{id}/archive"
