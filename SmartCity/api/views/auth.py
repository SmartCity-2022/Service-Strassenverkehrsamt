from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.jwt import verify

@api_view(["GET"])
def auth(request):
    status = verify(request)
    if status != 200:
        return Response({"auth": False}, status=200)
    return Response({"auth": True}, status=200)