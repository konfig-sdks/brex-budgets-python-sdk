operation_parameter_map = {
    '/v1/budget_programs-POST': {
        'parameters': [
            {
                'name': 'budget_blueprints'
            },
            {
                'name': 'name'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'description'
            },
            {
                'name': 'existing_budget_ids'
            },
            {
                'name': 'employee_filter'
            },
        ]
    },
    '/v1/budget_programs/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/budget_programs-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/budget_programs/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/budget_programs/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'description'
            },
            {
                'name': 'existing_budget_ids'
            },
            {
                'name': 'budget_blueprints'
            },
            {
                'name': 'employee_filter'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/v1/budgets/{id}/archive-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/budgets-POST': {
        'parameters': [
            {
                'name': 'parent_budget_id'
            },
            {
                'name': 'period_type'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'limit_type'
            },
            {
                'name': 'spend_type'
            },
            {
                'name': 'limit_visibility'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'owner_user_ids'
            },
            {
                'name': 'member_user_ids'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
        ]
    },
    '/v1/budgets/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/v1/budgets-GET': {
        'parameters': [
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v1/budgets/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'Idempotency-Key'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'owner_user_ids'
            },
            {
                'name': 'member_user_ids'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'limit_type'
            },
            {
                'name': 'spend_type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'limit_visibility'
            },
        ]
    },
};