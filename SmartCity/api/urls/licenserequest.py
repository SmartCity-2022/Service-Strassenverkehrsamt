from django.urls import path
from rest_framework import routers
from api.views import licenserequest


urlpatterns = [
     path("licenserequest/create", licenserequest.add_license_request),
     path("licenserequest/user/", licenserequest.get_license_requests_by_user),
     path("licenserequest/delete/<int:id>/", licenserequest.delete_license_request_by_id),
]