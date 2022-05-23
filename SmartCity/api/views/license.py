from rest_framework.response import Response
from rest_framework.decorators import api_view
from stva.models import License
from ..serializers import LicenseSerializer


@api_view(["GET"])
def get_all_licenses(request):
    licenses = License.objects.all()
    serializer = LicenseSerializer(licenses, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_license(request):
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
    
    # TODO: Verify user by token from request first
    
    try:
        licenses = License.objects.filter(owner=request.owner)    
    except License.DoesNotExist:
        return Response(status=404)        
    serializer = LicenseSerializer(licenses, many=True)
    return Response(serializer.data)


@api_view(["DELETE"])
def delete_license_by_id(request, id):
    
    # TODO: Verify user by token from request first
    
    try:
        license = License.objects.get(pk=id)    
    except License.DoesNotExist:
        return Response(status=404)   
    license.delete()
    return Response(status=200)