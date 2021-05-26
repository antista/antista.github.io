from apps.core.forms import EpidemicForm, CoefficientField


class SEIRSForm(EpidemicForm):
    alpha = CoefficientField(
        label='α',
        help_text='Коэффициент инкубационного периода (alpha)',
    )
    ksi = CoefficientField(
        label='ξ',
        help_text='Скорость потери иммунитета (ksi)',
    )
    field_order = [
        'N',
        'days',
        'beta',
        'gamma',
        'alpha',
        'ksi',
        'birth',
        'death',
    ]
