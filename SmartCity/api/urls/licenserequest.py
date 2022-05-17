from django.urls import path
from rest_framework import routers
from api.views import licenserequest


urlpatterns = [
     path("licenserequest", licenserequest.get_all_license_requests),
     path("licenserequest/create", licenserequest.add_license_request),
     path("licenserequest/<int:id>/", licenserequest.get_license_request_by_id),
     path("licenserequest/user/<int:id>/", licenserequest.get_license_requests_by_user),
     path("licenserequest/delete/<int:id>/", licenserequest.delete_license_request_by_id),
]