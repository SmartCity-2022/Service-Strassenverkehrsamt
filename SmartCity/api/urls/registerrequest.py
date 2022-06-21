from django.urls import path
from rest_framework import routers
from api.views import registerrequest


urlpatterns = [
     path("registerrequest/create", registerrequest.add_register_request),
     path("registerrequest/user/", registerrequest.get_register_requests_by_user),
     path("registerrequest/delete/<int:id>", registerrequest.delete_register_request_by_id),
]