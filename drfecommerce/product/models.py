from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

class Category(MPTTModel):
    
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    objects = ActiveQuerySet().as_manager()
    
    class MPTTMeta:
        order_insertation_by = ['name']
    
        
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    objects = ActiveQuerySet().as_manager()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name  = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    

    objects = ActiveQuerySet().as_manager()
    
    
    
    def __str__(self):
        return self.name   


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sku = models.CharField(max_length=100)
    stock = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_line')
    is_active = models.BooleanField(default=False)
    

    objects = ActiveQuerySet().as_manager()
   

    
    def __str__(self):
        return self.sku