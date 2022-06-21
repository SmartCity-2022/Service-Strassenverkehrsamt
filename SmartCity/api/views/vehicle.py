from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Vehicle
from api.jwt import verify, read_payload
from ..serializers import VehicleSerializer
import datetime


@api_view(["POST"])
def add_vehicle(request):
    status = verify(request)
    if status != 200:
        return Response(status=status)
    payload = read_payload(request)
    request.data["displacement"] = float(request.data["displacement"])
    request.data["emissions"] = float(request.data["emissions"])
    request.data["owner"] = payload["email"]
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=200)


@api_view(["GET"])
def get_vehicle_by_user(request):
    status = verify(request)
    if status != 200:
        return Response(status=status)
    try:
        payload = read_payload(request)
        vehicles = Vehicle.objects.filter(owner=payload["email"])    
    except Vehicle.DoesNotExist:
        return Response(status=404)        
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_vehicle_by_id(request, id):
    status = verify(request)
    if status != 200:
        return Response(status=status)
    try:
        vehicle = Vehicle.objects.get(pk=id)    
    except Vehicle.DoesNotExist:
        return Response(status=404)   
    vehicle.delete()
    return Response(status=200)
