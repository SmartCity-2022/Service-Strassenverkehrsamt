from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Vehicle
from ..serializers import VehicleSerializer


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
    
    # TODO: Verify user by token from request first
    
    try:
        vehicles = Vehicle.objects.filter(owner=request.owner)    
    except Vehicle.DoesNotExist:
        return Response(status=404)        
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_vehicle_by_id(request, id):
    
    # TODO: Verify user by token from request first
    
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