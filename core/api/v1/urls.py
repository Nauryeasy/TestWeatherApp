from django.urls import path

from core.api.v1.city.api_views import GetCitiesListApiView, GetWeatherForecastApiView

urlpatterns = [
    path('cities/', GetCitiesListApiView.as_view()),
    path('forecast/', GetWeatherForecastApiView.as_view()),
]
