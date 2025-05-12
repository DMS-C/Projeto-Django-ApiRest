from django.db import models
from customers.models import Customer
from cars.models import Car

# Create your models here.

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    sale_date = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Venda de {self.car} para {self.customer} em {self.sale_date}"
    
    