from django.urls import path

from apps.core.views import AboutView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
]