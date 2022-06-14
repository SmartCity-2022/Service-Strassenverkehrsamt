from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Licenserequest
from api.jwt import verify, read_payload
from ..serializers import LicenseRequestSerializer


@api_view(["GET"])
def get_all_license_requests(request):
    requests = Licenserequest.objects.all()
    serializer = LicenseRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_license_request(request):
    if not verify(request):
        return Response(status=400)
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
    if not verify(request):
        return Response(status=400)
    try:
        payload = read_payload(request)
        requests = Licenserequest.objects.filter(citizen=payload["email"])    
    except Licenserequest.DoesNotExist:
        return Response(status=404)        
    serializer = LicenseRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_license_request_by_id(request, id):
    if not verify(request):
        return Response(status=400)
    try:
        licenserequest = Licenserequest.objects.get(pk=id)    
    except Licenserequest().DoesNotExist:
        return Response(status=404)   
    licenserequest.delete()
    return Response(status=200)