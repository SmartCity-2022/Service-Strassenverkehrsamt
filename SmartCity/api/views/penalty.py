from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import Penalty
from ..serializers import PenaltySerializer


@api_view(["GET"])
def get_all_penaltys(request):
    penaltys = Penalty.objects.all()
    serializer = PenaltySerializer(penaltys, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_penalty(request):
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.headers["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    serializer = PenaltySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_penalty_by_id(request, id):
    try:
        penalty = Penalty.objects.get(pk=id)
    except Penalty.DoesNotExist:
        return Response(status=404)        
    serializer = PenaltySerializer(penalty, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_penalty_by_user(request):
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.headers["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        penalty = Penalty.objects.filter(owner=payload["email"])    
    except Penalty.DoesNotExist:
        return Response(status=404)        
    serializer = PenaltySerializer(penalty, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_penalty_by_id(request, id):
    if "accesToken" not in request.headers.keys():
        return Response(status=400) 
    payload = jwt.encode_token(request.headers["accessToken"])
    if not jwt.verify(payload["expireDate"]):
       return Response(status=401) 
    try:
        penalty = Penalty.objects.get(pk=id)    
    except Penalty.DoesNotExist:
        return Response(status=404)   
    penalty.delete()
    return Response(status=200)