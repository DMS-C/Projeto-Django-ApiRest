from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from django.db.models import Sum
from sales.models import Sale
from sales.serializers import SaleSerializer
from sales.permissions import IsSlaesOrAdminUser, IsCustomerOrAdminUser

class SaleListCreateView(ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (IsSlaesOrAdminUser, IsCustomerOrAdminUser)

class SaleRerieveView(RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (IsSlaesOrAdminUser, IsCustomerOrAdminUser)
    permission_classes = (IsSlaesOrAdminUser, IsCustomerOrAdminUser)
    permission_classes = (IsSlaesOrAdminUser, IsCustomerOrAdminUser)

class SaleReportView(ListAPIView):
    permission_classes = (IsSlaesOrAdminUser, IsCustomerOrAdminUser)

    def list(self, request, *args, **kwargs):
        total_sales = Sale.objects.count()
        total_revenue = Sale.objects.aggregate(total=Sum('value'))['total'] or 0
        report = {
            'total_sales': total_sales,
            'total_revenue': total_revenue,
        }
        return Response(report)