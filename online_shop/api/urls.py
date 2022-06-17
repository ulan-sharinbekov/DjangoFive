from django.urls import path, include
from rest_framework import routers

from api.views import CategoryAPIViewset, ProductAPIViewset, ProductAdd, RatingAPIView, CommentAPIView

router = routers.DefaultRouter()
router.register(r'category', CategoryAPIViewset, basename='category')
router.register(r'product', ProductAPIViewset, basename='product')

router.register(r'rating', RatingAPIView, basename='rating')
router.register(r'comment', CommentAPIView, basename='comment')

urlpatterns = [
    # path('rate/<int:pk>', RatingAPIView.as_view(), name='rating')
]

urlpatterns += router.urls
