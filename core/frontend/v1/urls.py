from django.urls import path

from core.frontend.v1.views import MainTemplateView

urlpatterns = [
    path('', MainTemplateView.as_view(), name='main'),
]
