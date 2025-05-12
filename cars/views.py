from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from cars.models import Car, Brand
from cars.serializers import CarSerializer, BrandSerializer
from cars.permissions import IsAdminOrReadOnly

class BrandCreateListView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAdminOrReadOnly)

class CarCreateListView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly)

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly)

class AvaliableCarView(ListAPIView):
    """ Lista todos os carros disponíveis no estoque """
    queryset = Car.objects.filter(status='available')
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated)

class SoldCarView(ListAPIView):
    """ Lista todos os carros vendidos """
    queryset = Car.objects.filter(status='sold')
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated)