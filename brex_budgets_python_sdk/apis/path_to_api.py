import typing_extensions

from brex_budgets_python_sdk.paths import PathValues
from brex_budgets_python_sdk.apis.paths.v1_budget_programs import V1BudgetPrograms
from brex_budgets_python_sdk.apis.paths.v1_budget_programs_id import V1BudgetProgramsId
from brex_budgets_python_sdk.apis.paths.v1_budgets import V1Budgets
from brex_budgets_python_sdk.apis.paths.v1_budgets_id import V1BudgetsId
from brex_budgets_python_sdk.apis.paths.v1_budgets_id_archive import V1BudgetsIdArchive

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_BUDGET_PROGRAMS: V1BudgetPrograms,
        PathValues.V1_BUDGET_PROGRAMS_ID: V1BudgetProgramsId,
        PathValues.V1_BUDGETS: V1Budgets,
        PathValues.V1_BUDGETS_ID: V1BudgetsId,
        PathValues.V1_BUDGETS_ID_ARCHIVE: V1BudgetsIdArchive,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_BUDGET_PROGRAMS: V1BudgetPrograms,
        PathValues.V1_BUDGET_PROGRAMS_ID: V1BudgetProgramsId,
        PathValues.V1_BUDGETS: V1Budgets,
        PathValues.V1_BUDGETS_ID: V1BudgetsId,
        PathValues.V1_BUDGETS_ID_ARCHIVE: V1BudgetsIdArchive,
    }
)
