from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Category, Brand, Product, ProductLine, ProductImage
# Register your models here.



class EditLinkInLine(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        
        if instance.pk:
            link=mark_safe('<a href="{u}">edit</a>'.format(u=url))
            return link
        else: 
            return "" 


class AdminProductImageInLine(admin.TabularInline):
    model = ProductImage

class AdminProductLineInLine(EditLinkInLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ('edit',)
    

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    inlines = [AdminProductLineInLine]
    list_display = ['id', 'name', 'is_digital', 'is_active', 'category']
    list_editable = ['is_digital', 'is_active']

@admin.register(ProductLine)
class AdminProductLine(admin.ModelAdmin):
    inlines = [AdminProductImageInLine]



class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    
class AdminBrand(admin.ModelAdmin):
    list_display = ['id', 'name']
    

admin.site.register(Category, AdminCategory)
admin.site.register(Brand, AdminBrand)
