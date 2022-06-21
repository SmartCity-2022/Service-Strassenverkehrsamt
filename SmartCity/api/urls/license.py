from django.urls import path
from rest_framework import routers
from api.views import license


urlpatterns = [
     path("license/create", license.add_license),
     path("license/user/", license.get_license_by_user)
]