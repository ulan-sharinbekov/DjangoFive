from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Brand, Vehicle
from api.serializers import BrandSerializer, VehicleSerializer
# Create your views here.


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated,)


class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class VehicleListAPIView(generics.ListAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        find = self.request.query_params.get('year')
        return Vehicle.objects.filter(year=find)

# class DataList(APIView):
#     def get(self, request):
#         return Response({'data': "Derbes Utebaliyev"})
#     def post(self, request):
#         title = request.data['title']
#         print(title)
#         return Response({'data2': "Derbes Utebaliyev"})
#
# class BrandAPIView(APIView):
#     def get(self, request):
#         list1 = Brand.objects.all()
#         q = BrandSerializer(list1, many=True)
#
#         print(q, type(q), q.data, sep='\n')
#         return Response({"data": q.data})
#
#     def post(self, request):
#         serializer = BrandSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#
#         return Response({"data": serializer.data})
#
# class BrandAPIViewDetailed(APIView):
#     def put(self, request, pk):
#         brand = Brand.objects.get(id=pk)
#         serializer = BrandSerializer(data=request.data, instance=brand)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response({"data": serializer.data})
#
#     def delete(self, request ,pk):
#         brand = Brand.objects.get(id=pk)
#         brand.delete()
#         return Response({"data": "deleted"})
