from django.urls import path
from rest_framework import routers
from api.views import license


urlpatterns = [
     path("license", license.get_all_licenses),
     path("license/create", license.add_license),
     path("license/<int:id>/", license.get_license_by_id),
     path("license/user/", license.get_license_by_user),
     path("license/delete/<int:id>/", license.delete_license_by_id),
]