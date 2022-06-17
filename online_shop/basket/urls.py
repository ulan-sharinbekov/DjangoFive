from django.urls import path

from rest_framework.routers import DefaultRouter

from basket.views import BasketAPIViewset, BasketProductAPIViewset, BasketProductAdd

router = DefaultRouter()
router.register(r'basket', BasketAPIViewset, basename='basket')
router.register(r'product', BasketProductAPIViewset, basename='basket_product')

urlpatterns = [
    path('product/add/<int:pk>', BasketProductAdd, name='product_add'),

]
urlpatterns += router.urls
print(router)
