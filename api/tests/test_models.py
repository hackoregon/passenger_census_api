from django.test import TestCase
from api.models import PassengerCensus

class PassengerCensusTest(TestCase):
    """ Test for PassengerCensus model """

    def setUp(self):
        PassengerCensus.objects.create(route_number=1547419)

    def test_route_number(self):
        route = PassengerCensus.objects.get(route_number=1547419)
        self.assertEqual(route.route_number, 1547419)