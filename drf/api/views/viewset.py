from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from api.models import Brand, Vehicle
from api.serializers import BrandSerializer, VehicleSerializer
# Create your views here.


class BrandAPIViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class VehicleAPIViewset(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer




class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
