from rest_framework.viewsets import ModelViewSet
from .models import Tour
from .serializers import TourSerializer
from .models import City
from .serializers import CitySerializer




class TourViewSet(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

