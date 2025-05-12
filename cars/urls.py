from django.urls import path
from cars.views import CarCreateListView, CarRetrieveUpdateDestroyView, BrandCreateListView, AvaliableCarView, SoldCarView

urlpatterns = [
    path('brands/', BrandCreateListView.as_view(), name='brand-list-create'),
    path('cars/', CarCreateListView.as_view(), name='car-list-create'),
    path('cars/<int:pk>/', CarRetrieveUpdateDestroyView.as_view(), name='car-retrieve-update-destroy'),
    path('stock/available/', AvaliableCarView.as_view(), name='available-cars'),
    path('stock/sold/', SoldCarView.as_view(), name='sold-cars'),
]