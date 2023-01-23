from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly,AllowAny


class product_datail(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = productserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class product_inventory_datail(viewsets.ModelViewSet):
    queryset = productinventory.objects.all()
    serializer_class = productinventoryserializer

class catagory_datail(viewsets.ModelViewSet):
    queryset = catagory.objects.all()
    serializer_class = catagoryserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class media_datail(viewsets.ModelViewSet):
    queryset = media.objects.all()
    serializer_class = mediaserializer

class stock_datail(viewsets.ModelViewSet):
    queryset = stock.objects.all()
    serializer_class = stockserializer
