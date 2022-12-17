from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from account.models import Create_Channel
from account.serializer import *
from django.contrib.auth.models import User
from rest_framework.authentication import (
    SessionAuthentication, 
    BasicAuthentication
    )
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from rest_framework.generics import  GenericAPIView
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework import status

class Register(ModelViewSet):
    queryset = Create_Channel.objects.all()
    serializer_class = Register_ser


from django.db.models import Q
class Is_Channel(CreateAPIView):
    
    queryset = Create_Channel.objects.all()
    serializer_class = Channel_Update_ser
   

   
    # def perform_update(self, serializer):
    #     users_id = int(self.kwargs.get('pk'))
    #     queryset = self.filter_queryset(self.queryset)
    #     queryset = queryset.get(
    #         Q(
    #             id=users_id
    #             ) & Q(
    #                 username=self.request.user
    #                 )
    #         )
    #     print(">>>>>>>>", self.request.user.username)    
        
    
   
   
    '''def update(self, request, *args, **kwargs):
        partial = True # Here I change partial to True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data) '''

class Login(GenericAPIView):
    
    serializer_class = Login_ser
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        print(">>>>>>", username)
        print(">>>>>>", password)
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'})
        user = authenticate(username=username, password=password)
        print(">>>>>", user)
        if user == None:
            return Response({'error': 'Invalid Credentials'})
        token, _ = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({'token': token.key})  



         
# skyakash
# psw : skyakash@123