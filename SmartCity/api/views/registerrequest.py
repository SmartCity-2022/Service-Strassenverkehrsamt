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
    
    # TODO: Verify user by token from request first
    
    try:
        requests = Registerrequest.objects.filter(owner=request.owner)    
    except Registerrequest.DoesNotExist:
        return Response(status=404)        
    serializer = RegisterRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_register_request_by_id(request, id):
    
    # TODO: Verify user by token from request first
    
    try:
        registerrequest = Registerrequest.objects.get(pk=id)    
    except Registerrequest.DoesNotExist:
        return Response(status=404)   
    registerrequest.delete()
    return Response(status=200)