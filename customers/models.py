from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cpf_cnpj = models.CharField(max_length=14, unique=True)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name