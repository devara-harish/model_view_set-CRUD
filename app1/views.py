from django.shortcuts import render

# Create your views here.

from app1.models import *
from app1.serializers import *

from rest_framework.response import Response

from rest_framework import viewsets

class ProductCrudOperations(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=productserializers
