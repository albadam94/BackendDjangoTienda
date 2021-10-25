from django.db import models

# Create your models here.
class Tienda(models.Model):
    Producto= models.CharField(max_length=100)
    Imagen= models.ImageField(upload_to='tienda/static/img/')
    Precio= models.IntegerField()
    Stock= models.IntegerField()
    Descripcion= models.TextField()
    Fecha= models.DateField()
    
    def __str__(self):
        return self.Producto
        
