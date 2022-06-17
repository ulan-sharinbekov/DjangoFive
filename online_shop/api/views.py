from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView

from django.db.models import Value, FloatField, Prefetch
from api.models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .service import ProductFilter, LargeResultsSetPagination


class CategoryAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        return CategorySerializer

    def get_queryset(self):
        # if(self.kwargs.get('pk')):
        #     return

        return Category.objects.all()
    

class ProductAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

    def get_serializer_class(self):
        # if(self.request.method == "POST"):
        #     print("PPPPP")
        if (self.kwargs.get('pk')):
            return ProductSerializer
        elif (self.request.method == "POST"):
            return ProductCreateSerializer
        return ProductSerializer

    def get_queryset(self):
        if(self.kwargs.get('pk')):
            pk = self.kwargs.get('pk')
            product = Product.objects.get(id=pk)
            ratings = Rating.objects.filter(product = product)
            avg = 0
            for item in ratings:
                avg = avg + item.grade

            Product.objects.filter(id=pk).update(ratingg = Value(avg/len(ratings)))
            print("here `11")
            return Product.objects.filter(id=pk)
        return Product.objects.all()

class ProductAdd():
    pass


class RatingAPIView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    serializer_class = RatingSerializer
    pagination_class = LargeResultsSetPagination
    # queryset = Rating.objects.all()

    def get_queryset(self):
        return Rating.objects.all()

    def perform_create(self, serializer):
        pk = self.request.data.get('product')
        product = Product.objects.get(id=pk)
        grade = float(self.request.data.get('grade'))
        print(grade)

        serializer.save(user=self.request.user)
        serializer.save(product=product)
        serializer.save(grade = grade)

        ratings = Rating.objects.filter(product=product)
        avg = 0
        for item in ratings:
            print(item.grade)
            avg = avg + item.grade
        res = (avg ) / (len(ratings) )
        print(res)
        Product.objects.filter(id=pk).update(ratingg=Value(res))

class CommentAPIView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        print(self.request.data.get('product'))
        product = Product.objects.get(id=self.request.data.get('product'))

        serializer.save(user=self.request.user)
        serializer.save(product=product)
        serializer.save(value=self.request.data.get('value'))
        if(self.kwargs.get('parent') == None):
            pass
        else:
            parentComment = Comment.objects.get(id=self.request.data.get('parent'))
            if(parentComment.get('parent') == None):
                serializer.save(parent=parentComment)
            else:
                serializer.save(parent=parentComment.get('parent'))
