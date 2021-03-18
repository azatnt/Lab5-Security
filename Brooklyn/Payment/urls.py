from django.urls import path
from .views import *

urlpatterns = [
    path('authorize/', authorize.as_view(), name='authorize_url'),
]
