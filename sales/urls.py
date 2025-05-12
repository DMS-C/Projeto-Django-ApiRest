from django.urls import path
from sales.views import SaleListCreateView, SaleRerieveView, SaleReportView

urlpatterns = [
    path('sales/', SaleListCreateView.as_view(), name='sale-list-create'),
    path('sales/<int:pk>/', SaleRerieveView.as_view(), name='sale-retrieve'),
    path('sales/report/', SaleReportView.as_view(), name='sales-report'),
]