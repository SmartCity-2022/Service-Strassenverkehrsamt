from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from stva.models import *

class BillTests(APITestCase):
    
    
    def test_get_bills(self):
        url = reverse('bill')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_bill_by_id(self):
        url = reverse('bill/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LicenseTests(ApiTestCast):
    
    
    def test_get_licenses(self):
        url = reverse('license')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_license_by_id(self):
        url = reverse('license/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class LicenseRequestTests(ApiTestCast):
    
    
    def test_get_licenses(self):
        url = reverse('licenserequest')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_license_by_id(self):
        url = reverse('licenserequest/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class PenaltyTests(ApiTestCast):
    
    
    def test_get_penaltys(self):
        url = reverse('penalty')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_license_by_id(self):
        url = reverse('penalty/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class RegisterRequestTests(ApiTestCast):
    
    
    def test_get_licenses(self):
        url = reverse('registerrequest')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_license_by_id(self):
        url = reverse('registerrequest/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
class VehicleTests(ApiTestCast):
    
    
    def test_get_penaltys(self):
        url = reverse('vehicle')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_get_license_by_id(self):
        url = reverse('vehicle/1')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
