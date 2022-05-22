from django.urls import path
from rest_framework import routers
from api.views import bill


urlpatterns = [
     path("bill", bill.get_all_bills),
     path("bill/create", bill.add_bill),
     path("bill/<int:id>/", bill.get_bill_by_id),
     path("bill/user/", bill.get_bill_by_user),
     path("bill/delete/<int:id>/", bill.delete_bill_by_id),
]