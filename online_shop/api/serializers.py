
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



class ProductShortSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'articule', 'currency', 'count', 'description', 'ratingg')


class ProductSerializer(ProductShortSerializer):
    category = CategorySerializer(read_only=True)
    class Meta(ProductShortSerializer.Meta):
        fields = ProductShortSerializer.Meta.fields + ('category',)

# class ProductRatingSerializer(ProductShortSerializer):
#     class Meta(ProductShortSerializer.Meta):
#         fields = ProductShortSerializer.Meta.fields + ('ratingg', )



class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
