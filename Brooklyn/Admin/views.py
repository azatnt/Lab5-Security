from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.shortcuts import redirect
from pyexcel_xls import get_data as xls_get
from pyexcel_xlsx import get_data as xlsx_get
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
import re
import xlrd
import datetime







@login_required(login_url="login/")

def index(request):
    context = {}
    return render(request, 'crmapp/index.html', context)


def login(request):
    return render(request, 'registration/login.html')



def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('username')
			return HttpResponseRedirect(reverse('home'))
	else:
		form = UserRegisterForm()
	return render(request, 'registration/register.html', context={'form':form})



def add_reestr(request):
    return render(request, 'add_reestr.html', context={})





class ParseExcelContact(APIView):
    def post(self, request, format=None):
        try:
            excel_file = request.FILES['files']
        except MultiValueDictKeyError:
            return redirect('add_reestr_url')
        if (str(excel_file).split('.')[-1] == "xls"):
            data = xls_get(excel_file, column_limit=16)
        elif (str(excel_file).split('.')[-1] == "xlsx"):
            data = xlsx_get(excel_file, column_limit=16)
        else:
            return redirect('add_reestr_url')
        com = data["контакты"]

        phone_name = com[1][8]
        phone_name2 = com[1][9]
        address_type1 = com[1][6]
        address_type2 = com[1][7]

        try:
            for i in range(2,len(com)):

                id_card_type = com[i][2]
                if id_card_type == 'Удост-ие личности гражданина РК':
                    id_card_type = 'Удостоверение личности'
                else:
                    pass
                r = DIdcardType.objects.filter(name=id_card_type)
                if (r.count() == 0):
                    DIdcardType.objects.create(
                        name = id_card_type,
                        status = 1,
                        desc = 'Id card type desc'
                    )
                else:
                    pass

                iin = str(com[i][0])

                issue_date = com[i][4]
                to_output = datetime.datetime.strptime(issue_date, "%d.%m.%Y")
                id_card_name = com[i][2]

                result = []
                phone2 = com[i][9]
                data = phone2.split(" ")
                data.pop(0)
                a = []
                list1 = []


                try:
                    queryset = TPersons.objects.get(iin=iin)
                    queryset_card = DIdcardType.objects.get(name=id_card_type)
                    queryset_phone_name1 = DPhoneType.objects.get(name=phone_name)

                    if i%2==0:
                        queryset_address_type = DAddressType.objects.get(name=address_type1)
                    else:
                        queryset_address_type = DAddressType.objects.get(name=address_type2)
                    try:
                        address = com[i][6]
                        address2 = com[i][7]
                        work = com[i][10]
                        id_card_num = com[i][3]
                        phone = com[i][8]


                        a = TAddresses.objects.get(address = address, id_person=queryset, id_address_type=queryset_address_type)
                        e = TAddresses.objects.get(address=address2, id_person=queryset)
                        b = TWork.objects.get(org_name = work, id_person=queryset)
                        c = TIdcard.objects.get(idcard_num = id_card_num, id_person=queryset, id_idcard_type=queryset_card)
                        d = TPhones.objects.get(phone_num = phone, id_person=queryset, id_phone_type=queryset_phone_name1)
                    except:
                        if i%2==0:
                            TAddresses.objects.create(
                                address = com[i][6],
                                id_person = queryset,
                                id_address_type = queryset_address_type,
                                status = 1,
                                desc = 'Contact desc'
                            )
                        else:
                            TAddresses.objects.create(
                                address = com[i-1][7],
                                id_person = queryset,
                                id_address_type = queryset_address_type,
                                status = 1,
                                desc = 'Contact desc'
                            )
                        try:
                            TWork.objects.create(
                                org_name = com[i][10],
                                id_person = queryset
                            )
                        except:
                            TWork.objects.create(
                                org_name = None,
                                id_person = queryset
                            )

                        TIdcard.objects.create(
                            idcard_num = com[i][3],
                            issue_date = to_output,
                            given_by = com[i][5],
                            id_person = queryset,
                            id_idcard_type = queryset_card,
                            desc = 'Id card desc'
                        )

                        TPhones.objects.create(
                            phone_num = com[i][8],
                            id_person = queryset,
                            id_phone_type = queryset_phone_name1,
                            desc = 'Mobile desc'
                        )
                except:
                    TAddresses.objects.create(
                        address = com[i][6],
                        id_person = None,
                        id_address_type = None,
                        status = 1,
                        desc = 'Contact desc'
                        )
                    TWork.objects.create(
                        org_name = com[i][10],
                        id_person = None,
                    )
                    TIdcard.objects.create(
                        idcard_num = com[i][3],
                        issue_date = to_output,
                        given_by = com[i][5],
                        id_person = None,
                        id_idcard_type = None,
                        desc = 'Id card desc'
                    )
                    TPhones.objects.create(
                        phone_num = com[i][8],
                        id_person = None,
                        id_phone_type = None,
                        desc = 'Mobile desc'
                    )

        except:
            return HttpResponseRedirect(reverse('add_reestr_url'))

        return render(request, 'add_reestr.html', context={})







class ParseExcel(APIView):
    def post(self, request, format=None):
        try:
            excel_file = request.FILES['files']
        except MultiValueDictKeyError:
            return redirect('add_reestr_url')
        if (str(excel_file).split('.')[-1] == "xls"):
            data = xls_get(excel_file, column_limit=16)
        elif (str(excel_file).split('.')[-1] == "xlsx"):
            data = xlsx_get(excel_file, column_limit=16)
        else:
            return redirect('add_reestr_url')
        com = data["list1"]
        a = []
        try:
            for i in range(5,len(com)):
                region = com[i][1]
                r = DRegions.objects.filter(name=region)
                if (r.count() == 0):
                    DRegions.objects.create(
                        name = com[i][1],
                        status = 1,
                        desc = 'some description'
                    )
                else:
                    pass

                region = com[i][1]
                full_name = com[i][3]
                name_surname = full_name.split(" ")
                to_output = name_surname[0] + " " + name_surname[1] + " " + name_surname[-1]
                try:
                    queryset = DRegions.objects.get(name=region)
                    try:
                        iin = com[i][4]
                        a = TPersons.objects.get(iin = iin, id_region=queryset)
                    except:
                        TPersons.objects.create(
                            name = name_surname[1],
                            surname = name_surname[0],
                            patronymic = name_surname[-1],
                            iin = com[i][4],
                            full_name = com[i][3],
                            id_region = queryset,
                            status = 1,
                            desc = 'Persons desc',
                            id_rollback = 1,
                        )
                except:
                    pass

                iin = com[i][4]
                try:
                    issue_date = com[i][5]
                    close_date = com[i][6]
                    to_output_issue = datetime.datetime.strptime(issue_date, "%d.%m.%Y")
                    to_output_close = datetime.datetime.strptime(close_date, "%d.%m.%Y")
                    queryset = TPersons.objects.get(iin=iin)
                    try:
                        agr_num = com[i][2]
                        a = TDebtData.objects.get(agr_num = agr_num, id_person=queryset)
                    except:
                        TDebtData.objects.create(
                            agr_num = com[i][2],
                            issue_date = to_output_issue,
                            close_date = to_output_close,
                            overdue_day = com[i][7],
                            loan_amount = com[i][8],
                            claim_date = com[i][9],
                            total_amount = com[i][10],
                            claim_amount = com[i][11],
                            id_person = queryset,
                            main_debt = com[i][12],
                            percentage_debt = com[i][13],
                            fine_debt = com[i][14],
                            indebt_debt = com[i][15],
                            desc = 'Debt data desc'
                        )
                except:
                    TDebtData.objects.create(
                        agr_num = com[i][2],
                        issue_date = to_output_issue,
                        close_date = to_output_close,
                        overdue_day = com[i][7],
                        loan_amount = com[i][8],
                        claim_date = com[i][9],
                        id_person = None,
                        total_amount = com[i][10],
                        claim_amount = com[i][11],
                        main_debt = com[i][12],
                        percentage_debt = com[i][13],
                        fine_debt = com[i][14],
                        indebt_debt = com[i][15],
                        desc = 'Debt data desc'
                    )
        except IndexError:
            return HttpResponseRedirect(reverse('add_reestr_url'))

        return render(request, 'add_reestr.html', context={})
