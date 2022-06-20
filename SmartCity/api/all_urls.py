from django.urls import path, include
from rest_framework import routers
from . import views
from api.urls import *
from api.views import auth

urlpatterns = [
    path("", include("api.urls.bill")),
    path("", include("api.urls.license")),
    path("", include("api.urls.licenserequest")),
    path("", include("api.urls.registerrequest")),
    path("", include("api.urls.penalty")),
    path("", include("api.urls.vehicle")),
    path("auth", auth.auth)
]
