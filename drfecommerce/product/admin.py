from django.contrib import admin
from .models import Category, Brand, Product, ProductLine
# Register your models here.



class AdminProductLine(admin.TabularInline):
    model = ProductLine



class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    
class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [AdminProductLine]
    list_display = ['id', 'name', 'is_digital', 'is_active', 'category']
    list_editable = ['is_digital', 'is_active']
    

admin.site.register(Category, AdminCategory)
admin.site.register(Brand, AdminBrand)
