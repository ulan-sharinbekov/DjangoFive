from rest_framework import serializers

from basket.models import Basket, BasketProduct
from api.serializers import ProductSerializer
from _auth.serializers import UserShortSerializer

class BasketSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)
    class Meta:
        model = Basket
        # fields = ('id', 'user_id')
        fields = '__all__'

class BasketProductSerializer(serializers.ModelSerializer):
    basket_id = BasketSerializer(read_only=True)
    product_id = ProductSerializer(read_only=True)

    class Meta:
        model = BasketProduct
        fields = ('basket_id', 'product_id')

class BasketProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketProduct
        fields = '__all__'
