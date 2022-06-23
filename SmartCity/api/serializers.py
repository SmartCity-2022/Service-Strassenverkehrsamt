from rest_framework import serializers
from stva.models import *


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ["id", "value", "description", "receiver", "deadline"]


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ["id", "owner", "type", "received"]
        
        
class LicenseRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licenserequest
        fields = ["id", "citizen", "form", "issued", "licenseclass", "status"]
        
        
class PenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Penalty
        fields = ["id", "owner", "received", "value", "reason"]
        
        
class RegisterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registerrequest
        fields = ["id", "registration1", "registration2", "vehicle", "hucertificate", "status", "owner"]
        
        

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ["id", "brand", "model", "firstregistration", "displacement", "fueltype", "emissions", "hudeadline", "licenseplate", "owner"]