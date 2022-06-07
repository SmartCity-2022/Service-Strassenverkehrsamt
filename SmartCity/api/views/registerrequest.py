from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Registerrequest
from ..serializers import RegisterRequestSerializer


@api_view(["GET"])
def get_all_register_requests(request):
    requests = Registerrequest.objects.all()
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_register_request(request):
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
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
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        requests = Registerrequest.objects.filter(owner=payload["email"])    
    except Registerrequest.DoesNotExist:
        return Response(status=404)        
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_register_request_by_id(request, id):
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.META["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        registerrequest = Registerrequest.objects.get(pk=id)    
    except Registerrequest.DoesNotExist:
        return Response(status=404)   
    registerrequest.delete()
    return Response(status=200)