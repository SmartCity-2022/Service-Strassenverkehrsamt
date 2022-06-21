from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Registerrequest
from api.jwt import verify, read_payload
from ..serializers import RegisterRequestSerializer


@api_view(["POST"])
def add_register_request(request):
    status = verify(request)
    if status != 200:
        return Response(status=status)
    request.data["status"] = "In Bearbeitung"
    serializer = RegisterRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_register_requests_by_user(request):
    status = verify(request)
    if status != 200:
        return Response(status=status)
    try:
        payload = read_payload(request)
        requests = Registerrequest.objects.filter(owner=payload["email"])    
    except Registerrequest.DoesNotExist:
        return Response(status=404)        
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_register_request_by_id(request, id):
    status = verify(request)
    if status != 200:
        return Response(status=status)
    try:
        registerrequest = Registerrequest.objects.get(pk=id)    
    except Registerrequest.DoesNotExist:
        return Response(status=404)   
    registerrequest.delete()
    return Response(status=200)