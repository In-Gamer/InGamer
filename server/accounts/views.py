from django.shortcuts import render
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from rest_framework import generics, status
from rest_framework.response import Response


class RegisterView(generics.CreateAPIView):
  def post(self, request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({'message':'회원가입 성공'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class LoginView(generics.GenericAPIView):
  def post(self, request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
      return Response(serializer.validated_data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)