from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Vehicle
from api.jwt import verify, read_payload
from ..serializers import VehicleSerializer
import datetime


@api_view(["GET"])
def get_all_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_vehicle(request):
    if not verify(request):
        return Response(status=400)
    payload = read_payload(request)
    request.data["displacement"] = float(request.data["displacement"])
    request.data["emissions"] = float(request.data["emissions"])
    request.data["owner"] = payload["email"]
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=200)


@api_view(["GET"])
def get_vehicle_by_id(request, id):
    try:
        vehicle = Vehicle.objects.get(pk=id)    
    except Vehicle.DoesNotExist:
        return Response(status=404)        
    serializer = VehicleSerializer(vehicle, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_vehicle_by_user(request):
    if not verify(request):
        return Response(status=400)
    try:
        vehicles = Vehicle.objects.filter(owner=payload["email"])    
    except Vehicle.DoesNotExist:
        return Response(status=404)        
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_vehicle_by_id(request, id):
    if not verify(request):
        return Response(status=400)
    try:
        vehicle = Vehicle.objects.get(pk=id)    
    except Vehicle.DoesNotExist:
        return Response(status=404)   
    vehicle.delete()
    return Response(status=200)


@api_view(["PATCH"])
def patch_vehicle_by_id(request, id):
    
    # TODO: Verify user by token from request first
    # TODO: Algorithm to update dataset
    
    Vehicle.objects.get(pk=id).update()
    
    return Response(status=200)