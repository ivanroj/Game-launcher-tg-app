from django.urls import path
from . import views


urlpatterns = [
    path('', views.miniapp_home, name='home'),
]