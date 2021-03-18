from django.urls import path
from .views import *
from django.conf.urls import include
from Payment.views import *



urlpatterns = [
    path('', index, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register_url'),
    path('add_reestr/', add_reestr, name='add_reestr_url'),
    path('parse_excel_data/', ParseExcel.as_view(), name='parse_excel_url'),
    path('parse_excel_contact/', ParseExcelContact.as_view(), name='parse_excel_contact_url'),


]
