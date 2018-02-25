from api.models import PassengerCensus
from rest_framework.decorators import api_view, detail_route
from api.serializers import PassengerCensusSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


class PassengerCensusViewSet(viewsets.ModelViewSet):

    queryset = PassengerCensus.objects.all()
    serializer_class = PassengerCensusSerializer
    filter_backends = (SearchFilter,DjangoFilterBackend,OrderingFilter,)
    search_fields = ('route_number', 'direction','service_key','stop_seq',
                     'location_id','public_location_description',)
    filter_fields = ('summary_begin_date','route_number','direction','service_key','stop_seq','location_id',
                    'public_location_description','ons','offs','x_coord','y_coord','geom_2913','geom_4326',)
    ordering_fields = '__all__'

