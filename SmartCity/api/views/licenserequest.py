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
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
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
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        requests = Licenserequest.objects.filter(citizen=payload["email"])    
    except Licenserequest.DoesNotExist:
        return Response(status=404)        
    serializer = LicenseRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_license_request_by_id(request, id):
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        licenserequest = Licenserequest.objects.get(pk=id)    
    except Licenserequest().DoesNotExist:
        return Response(status=404)   
    licenserequest.delete()
    return Response(status=200)