from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView,BillCreateAPIView, BillRetrieveUpdateAPIView, EmployeeListCreateAPIView


urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<uuid:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-retrieve-update-destroy'),
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list-create'),
    path('customers/<uuid:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy'),
    path('bills/', BillCreateAPIView.as_view(), name='bill-create'),
    path('bills/<uuid:pk>/', BillRetrieveUpdateAPIView.as_view(), name='bill-retrieve-update'),
    path('employees/', EmployeeListCreateAPIView.as_view(), name='employee-list-create'),
]

