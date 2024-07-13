# store/serializers.py
from rest_framework import serializers
from .models import Product, Review, Wishlist
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'


# store/serializers.py
class ReviewSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField(many=False)
    class Meta:
        model = Review
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
# store/serializers.py
class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'
