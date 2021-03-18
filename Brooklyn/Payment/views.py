from django.shortcuts import render
from rest_framework.views import APIView
from requests import Request, post
from .credentials import *
from rest_framework.response import Response
from rest_framework import status





class authorize(APIView):
    def post(self, request, format=None):
         response = post('https://10.1.96.75/bcc/production/v1/oauth2/token',
         data={
            'redirect_uri': REDIRECT_URI,
            'client_id':'c11257dc-846b-4da1-b986-d7268875ecb3',
            'client_secret':'Q4rS4rX4bO7sI0wN1mL3wR0dV8hX3xI8lD2xT4qA1tW8wA7wA0',
            }).json()
         access_token = response.get('access_token')
         print(access_token)
         print(response)
         error = response.get('error')
         print(error)
         return Response({'token': access_token}, status=status.HTTP_200_OK)
