from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.


class CustomUserViewSet(GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED )
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self,request):
        serializer = self.serializer_class(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

    def get_permissions(self):
        if self.action in ['list','retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]