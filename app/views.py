from django.shortcuts import render
from rest_framework import generics,permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Product, Bill, Employee
from .serializers import ProductSerializer, CustomerSerializer, BillSerializer,EmployeeSerializer
from drf_spectacular.utils import extend_schema

class IsStaffPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class CustomerListCreateAPIView(generics.ListCreateAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsStaffPermission]

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsStaffPermission]

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffPermission]

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsStaffPermission]

class BillCreateAPIView(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsStaffPermission]

class BillRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsStaffPermission]


class EmployeeListCreateAPIView(generics.ListCreateAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAdminUser]
