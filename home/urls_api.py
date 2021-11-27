from django.urls import path

from home.views_api import LoginView
from .views_api import *

urlpatterns = [
    path("login/", LoginView),
    path("register/", RegisterView)
]