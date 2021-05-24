from apps.core.forms import EpidemicForm, CoefficientField, EpidemicVitalForm


class SEIRForm(EpidemicForm):
    alpha = CoefficientField(
        label='α',
        help_text='Коэффициент инкубационного периода (alpha)',
    )


class SEIRVForm(EpidemicVitalForm, SEIRForm):
    pass
