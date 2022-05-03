from django.urls import path
from rest_framework import routers
from . import views


urlpatterns = [
     path("bill", views.get_all_bills),
     path("bill/create", views.add_bill),
     path("license", views.get_all_licenses),
     path("license/create", views.add_license),
     path("licenserequest", views.get_all_license_requests),
     path("licenserequest/create", views.add_license_request),
     path("vehicle", views.get_all_vehicles),
     path("vehicle/create", views.add_vehicle),
     path("registerrequest", views.get_all_register_requests),
     path("registerrequest/create", views.add_register_request),
     path("penalty", views.get_all_penaltys),
     path("penalty/create", views.add_penalty),
]
