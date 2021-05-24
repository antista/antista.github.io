from django.shortcuts import render
from django.urls import reverse_lazy

from apps.core import constants
from apps.core.views import EpidemicModelView
from apps.sir.diffs import get_dots
from apps.sir.forms import SIRForm, SIRVForm

DEFAULT_FORM = SIRForm({
    'N': constants.DEFAULT_POPULATION,
    'days': constants.DEFAULT_DAYS,
    'beta': constants.DEFAULT_BETA,
    'gamma': constants.DEFAULT_GAMMA,
})

DEFAULT_VITAL_FORM = SIRVForm({
    'N': constants.DEFAULT_POPULATION,
    'days': constants.DEFAULT_DAYS,
    'beta': constants.DEFAULT_BETA,
    'gamma': constants.DEFAULT_GAMMA,
    'birth': constants.DEFAULT_BIRTH,
    'death': constants.DEFAULT_DEATH,
})


class SIRView(EpidemicModelView):
    template_name = 'sir.html'
    form_class = SIRForm
    success_url = reverse_lazy('sir:plot')
    default_form = DEFAULT_FORM
    model_name = 'SIR'

    def _get_response_data(self, request, form):
        form.get_prepared_form()
        y_S, y_I, y_R = get_dots(form)
        # y_S = [list(a) for a in zip(range(form.days), y_S)]
        # y_I = [list(a) for a in zip(range(form.days), y_I)]
        # y_R = [list(a) for a in zip(range(form.days), y_R)]
        return render(
            request,
            self.template_name,
            self.get_context_dict(form, y_S=y_S, y_I=y_I, y_R=y_R),
        )


class SIRVView(EpidemicModelView):
    template_name = 'sir.html'
    form_class = SIRVForm
    success_url = reverse_lazy('sir:vital')
    default_form = DEFAULT_VITAL_FORM
    model_name = 'SIR'
    vital = True

    def _get_response_data(self, request, form):
        form.get_prepared_form()
        y_S, y_I, y_R = get_dots(form, True)
        return render(
            request,
            self.template_name,
            self.get_context_dict(form, y_S=y_S, y_I=y_I, y_R=y_R),
        )
