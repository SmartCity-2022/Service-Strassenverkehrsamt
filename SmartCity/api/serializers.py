from rest_framework import serializers
from stva.models import *


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["value", "description", "receiver", "deadline"]


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ["owner", "type", "received"]
        
        
class LicenseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenserequest
        fields = ["citizen", "form", "issued"]
        
        
class PenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Penalty
        fields = ["owner", "received", "value", "reason"]
        
        
class RegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registerrequest
        fields = ["registration1", "registration2", "vehicle", "huCertificate"]
        
        
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["brand", "model", "firstregistration", "displacement", "fueltype", "emissions", "hudeadline", "licenseplate", "owner"]
        