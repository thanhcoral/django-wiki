from rest_framework.urls import path

from . import views


urlpatterns = [
    path('', views.RegisterView.as_view(), name='register')
]
