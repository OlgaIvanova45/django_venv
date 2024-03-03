from rest_framework import serializers
from ..models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'author_teacher', 'title', 'start_date', 'start_time', 'price')