from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import *
from .serializers import *

@api_view(["GET"])
def get_all_bills(request):
    bills = Bill.objects.all()
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_bill(request):
    serializer = BillSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_all_licenses(request):
    licenses = License.objects.all()
    serializer = LicenseSerializer(licenses, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_license(request):
    serializer = LicenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_all_license_requests(request):
    requests = Licenserequest.objects.all()
    serializer = LicenseRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_license_request(request):
    serializer = LicenseRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_all_penaltys(request):
    penaltys = Penalty.objects.all()
    serializer = PenaltySerializer(penaltys, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_penalty(request):
    serializer = PenaltySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_all_register_requests(request):
    requests = Registerrequest.objects.all()
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_register_request(request):
    serializer = RegisterRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_all_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
