from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import License
from api.jwt import verify, read_payload
from ..serializers import LicenseSerializer


@api_view(["GET"])
def get_all_licenses(request):
    licenses = License.objects.all()
    serializer = LicenseSerializer(licenses, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_license(request):
    if not verify(request):
        return Response(status=400)
    serializer = LicenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def get_license_by_id(request, id):
    try:
        license = License.objects.get(pk=id)
    except License.DoesNotExist:
        return Response(status=404)
    serializer = LicenseSerializer(license, many=False)
    return Response(serializer.data)


@api_view(["GET"])
def get_license_by_user(request):
    if not verify(request):
        return Response(status=400)
    try:
        payload = read_payload(request)
        licenses = License.objects.filter(owner=payload["email"])    
    except License.DoesNotExist:
        return Response(status=404)        
    serializer = LicenseSerializer(licenses, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_license_by_id(request, id):
    if not verify(request):
        return Response(status=400)
    try:
        license = License.objects.get(pk=id)    
    except License.DoesNotExist:
        return Response(status=404)   
    license.delete()
    return Response(status=200)