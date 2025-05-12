"""""
import json
from django.http import JsonResponse
from customers.models import Customer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@csrf_exempt
def customer_view(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        data = {
            'customers': list(customers.values())
        }
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_customer = Customer(
            name=data['name'],
            cpf_cnpj=data['cpf_cnpj'],
            contact=data['contact'],
            address=data['address']
        )
        new_customer.save()
        return JsonResponse(
            data,
            status=201,  # Created
        )

@csrf_exempt
def customer_detail_view(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'GET':
        data = {
            'name': customer.name,
            'cpf_cnpj': customer.cpf_cnpj,
            'contact': customer.contact,
            'address': customer.address
        }
        return JsonResponse(data)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        customer.name = data['name']
        customer.cpf_cnpj = data['cpf_cnpj']
        customer.contact = data['contact']
        customer.address = data['address']
        customer.save()
        return JsonResponse(data, status=200)
    elif request.method == 'DELETE':
        customer.delete()
        return JsonResponse({'message:' 'Customer deleted successfully'}, status=204)

"""

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from customers.models import Customer
from customers.serializers import CustomerSerializer
from customers.permissions import IsCustomerOrAdmin

class CustomerCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsCustomerOrAdmin)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsCustomerOrAdmin)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer