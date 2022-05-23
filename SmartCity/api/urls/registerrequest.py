from django.urls import path
from rest_framework import routers
from api.views import registerrequest


urlpatterns = [

     path("registerrequest", registerrequest.get_all_register_requests),
     path("registerrequest/create", registerrequest.add_register_request),
     path("registerrequest/<int:id>/", registerrequest.get_register_request_by_id),
     path("registerrequest/user/<int:id>/", registerrequest.get_register_requests_by_user),
     path("registerrequest/delete/<int:id>/", registerrequest.delete_register_request_by_id),
]