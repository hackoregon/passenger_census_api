from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'passenger-census', views.PassengerCensusViewSet)

#schema view
#schema_view = get_schema_view(title='ODOT Crash API')
schema_view = get_swagger_view(title='Passenger Census API')

urlpatterns = [
    url(r'^schema/', schema_view),
    url(r'^api/', include(router.urls)),
]