import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import PassengerCensus
from api.serializers import PassengerCensusSerializer

class PassengerCensusTest(APITestCase):
    
    def setUp(self):
        PassengerCensus.objects.create(route_number=1234)

    def test_passenger_census_serializer(self):
        """
        Ensure that serializer data matches the response data
        """
        route_obj = PassengerCensus.objects.get(route_number=1234)
        route_id = route_obj.id
        response = self.client.get('/api/passenger-census/'+ str(route_id) + '/')
        serializer = PassengerCensusSerializer(route_obj)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_passenger_census_permissions(self):
        """
        Ensure that unauthenticated users cannot create new records
        """
        response = self.client.post('/api/passenger-census/', {'route_number':1234}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        