from django.contrib import admin
from .models import Category, Brand, Product
# Register your models here.




class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    
class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminProduct(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_digital', 'category']


admin.site.register(Category, AdminCategory)
admin.site.register(Brand, AdminBrand)
admin.site.register(Product, AdminProduct)