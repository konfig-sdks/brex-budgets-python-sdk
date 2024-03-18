import typing_extensions

from brex_budgets_python_sdk.apis.tags import TagValues
from brex_budgets_python_sdk.apis.tags.budgets_api import BudgetsApi
from brex_budgets_python_sdk.apis.tags.budget_programs_api import BudgetProgramsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BUDGETS: BudgetsApi,
        TagValues.BUDGET_PROGRAMS: BudgetProgramsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BUDGETS: BudgetsApi,
        TagValues.BUDGET_PROGRAMS: BudgetProgramsApi,
    }
)
