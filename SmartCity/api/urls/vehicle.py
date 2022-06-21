from django.urls import path
from rest_framework import routers
from api.views import vehicle


urlpatterns = [
     path("vehicle/create", vehicle.add_vehicle),
     path("vehicle/user/", vehicle.get_vehicle_by_user),
     path("vehicle/delete/<int:id>", vehicle.delete_vehicle_by_id),
]