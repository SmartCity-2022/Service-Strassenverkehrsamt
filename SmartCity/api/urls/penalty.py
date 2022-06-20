from django.urls import path
from rest_framework import routers
from api.views import penalty


urlpatterns = [
     path("penalty", penalty.get_all_penaltys),
     path("penalty/create", penalty.add_penalty),
     path("penalty/<int:id>/", penalty.get_penalty_by_id),
     path("penalty/user/", penalty.get_penalty_by_user),
     path("penalty/delete/<int:id>/", penalty.delete_penalty_by_id),
]