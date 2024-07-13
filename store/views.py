from django.shortcuts import render
from rest_framework import viewsets



# Create your views here.
# store/views.py
from rest_framework import generics, filters
from .models import Product, Review, Wishlist
from .serializers import ProductSerializer, ProductDetailSerializer,ReviewSerializer, WishlistSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price', 'popularity']
    search_fields = ['size', 'color']
    
    


# store/views.py
class ProductDetailView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


# store/views.py
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
