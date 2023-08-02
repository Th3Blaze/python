from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField( max_length=200)
    pais=models.CharField(max_length=200)
    email=models.EmailField()

    def __str__(self):
        return self.nombre
    
class Venta(models.Model):
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto_vendido=models.CharField(max_length=200)
    monto=models.DecimalField(max_digits=10,decimal_places=2)
    fecha=models.DateField()

    def __str__(self):
        return f"{self.cliente} : {self.producto_vendido}"
    