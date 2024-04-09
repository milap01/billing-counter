from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def routes(request):
    
    if request.method == 'GET':
        
        return Response({
            '/api' : [
                'products/',
                'products/<uuid:pk>/',
                'customers/',
                'bills/',
                'bills/<uuid:pk>/',
                'employees/'
            ],
            '/' : [
                'swagger<format>/',
                'swagger/',
                'redoc/'
            ]
        })
