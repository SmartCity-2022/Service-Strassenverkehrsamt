from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Registerrequest
from api.jwt import verify, read_payload
from ..serializers import RegisterRequestSerializer


@api_view(["GET"])
def get_all_register_requests(request):
    requests = Registerrequest.objects.all()
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_register_request(request):
    if not verify(request):
        return Response(status=400)
    serializer = RegisterRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_register_request_by_id(request, id):
    try:
        registerrequest = Registerrequest.objects.get(pk=id)
    except Registerrequest.DoesNotExist:
        return Response(status=404)        
    serializer = RegisterrequestSerializer(registerrequest, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_register_requests_by_user(request):
    if not verify(request):
        return Response(status=400)
    try:
        payload = read_payload(request)
        requests = Registerrequest.objects.filter(owner=payload["email"])    
    except Registerrequest.DoesNotExist:
        return Response(status=404)        
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_register_request_by_id(request, id):
    if not verify(request):
        return Response(status=400)
    try:
        registerrequest = Registerrequest.objects.get(pk=id)    
    except Registerrequest.DoesNotExist:
        return Response(status=404)   
    registerrequest.delete()
    return Response(status=200)