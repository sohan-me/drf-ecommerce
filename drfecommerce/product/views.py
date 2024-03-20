from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer

# Create your views here.

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    


class BrandView(viewsets.ViewSet):
    queryset = Brand.objects.all()
    
    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
class ProductView(viewsets.ViewSet):
    
    # Only active product using IsActive Custom Manager
    queryset = Product.objects.active()
    
    lookup_field = 'slug'
    serializer_class = ProductSerializer
    
    @extend_schema(responses=serializer_class)
    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, slug=None):
        serializer = self.serializer_class(self.queryset.get(slug=slug))
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False, url_path=r'category/(?P<category>\w+)/all', url_name='all')
    def product_by_category(self, request, category=None):
        serializer = self.serializer_class(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
    
    
    