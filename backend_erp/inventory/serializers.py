from rest_framework import serializers
from .models import Material, Product

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = [
            'material_id',
            'name',
            'category',
            'image',
            'price',
            'stock',
            'unitcount',
            'location',
            'description',
            'expiredate',
            'isAvailable'
        ]

class ProductSerializer(serializers.ModelSerializer):
    materials = serializers.PrimaryKeyRelatedField(many=True, queryset=Material.objects.all())
    class Meta:
        model = Product
        fields = [
            'product_id',
            'name',
            'category',
            'materials',
            'sellingPrice',
            'stock',
            'location',
            'description',
            'image',
            'expiredate',
            'isAvailable'
        ]
