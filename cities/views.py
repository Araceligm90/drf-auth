from rest_framework import generics
from .serializers import CitySerializer
from .models import City
from .permissions import IsOwnerOrReadOnly


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = City.objects.all()
    serializer_class = CitySerializer
