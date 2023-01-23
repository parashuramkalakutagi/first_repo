from rest_framework import serializers
from .models import *

class catagoryserializer(serializers.ModelSerializer):
    class Meta:
        model = catagory
        fields = '__all__'


class productserializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class productinventoryserializer(serializers.ModelSerializer):
    class Meta:
        model = productinventory
        fields = '__all__'


class mediaserializer(serializers.ModelSerializer):
    class Meta:
        model = media
        fields = '__all__'

class stockserializer(serializers.ModelSerializer):
    class Meta:
        model = stock
        fields = '__all__'
