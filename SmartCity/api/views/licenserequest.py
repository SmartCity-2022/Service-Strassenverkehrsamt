from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Licenserequest
from ..serializers import LicenseRequestSerializer


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
def get_license_request_by_id(request, id):
    try:
        licenserequest = Licenserequest.objects.get(pk=id)
    except Licenserequest.DoesNotExist:
        return Response(status=404)        
    serializer = LicenserequestSerializer(licenserequest, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_license_requests_by_user(request):
    
    # TODO: Verify user by token from request first
    
    try:
        requests = Licenserequest.objects.filter(owner=request.owner)    
    except Licenserequest.DoesNotExist:
        return Response(status=404)        
    serializer = LicenseRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_license_request_by_id(request, id):
    
    # TODO: Verify user by token from request first
    
    try:
        licenserequest = Licenserequest.objects.get(pk=id)    
    except Licenserequest().DoesNotExist:
        return Response(status=404)   
    licenserequest.delete()
    return Response(status=200)