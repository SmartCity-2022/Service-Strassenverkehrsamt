from django.urls import path
from rest_framework import routers
from api.views import penalty


urlpatterns = [
     path("penalty/user/", penalty.get_penalty_by_user)
]