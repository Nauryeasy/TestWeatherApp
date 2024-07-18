from django.urls import path, include


urlpatterns = [
    path('', include('core.frontend.v1.urls')),
]
