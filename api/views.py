from django.shortcuts import render
from .models import Productos
from .serial import ProductosSerializer
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all().order_by('-fecha_creacion')
    serializer_class = ProductosSerializer