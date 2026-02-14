import os
import requests
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .import_requests import main


# Create your views here.

def redirect_request(request):
    return redirect('temperature-request', permanent=True)


@login_required
def temperature_request(request):
    input_list = []
    
    # user_room_input = request.GET.get('room_input', '')
    # user_input1 = request.GET.get('input1', '')
    # user_input2 = request.GET.get('input2', '')
    # user_input3 = request.GET.get('input3', '')
    # user_input4 = request.GET.get('input4', '')
    # user_input5 = request.GET.get('input5', '')
    # user_input6 = request.GET.get('input6', '')
    # user_input7 = request.GET.get('input7', '')
    # user_input8 = request.GET.get('input8', '')
    # user_input9 = request.GET.get('input9', '')
    # user_input10 = request.GET.get('input10', '')
    
    user_room_input = '3b0ef5f0-b51d-46d1-a487-a306936391c9'
    user_input1 = '45ad8ec0-6990-4107-adc7-d09699346580'
    user_input2 = '31bc6c73-38c5-4c6c-ae1e-574a83fcf87d'
    user_input3 = 'd8f58c6b-45e3-4062-a91e-8aaa19c0d2b2'
    user_input4 = '7e0539dd-5114-45c3-b55e-4f4c6a929891'
    user_input5 = 'f39ea2fc-5d54-4802-a63e-dcfb0c2c1d15'
    user_input6 = 'b4dc688a-f6f9-498f-9137-06cb60f1f0b3'
    # user_input7 = '31b1aef9-657d-4d04-a7c0-d81944205620'
    # user_input8 = 'b7854ac1-650e-425b-b4c5-e9c9523c2331'
    # user_input9 = 'c89cf283-8368-4225-8642-c436c33d0052'
    # user_input10 = '24c18b89-34c6-4b60-b9e6-8a9577a04feb'

    
    result = None

    if user_room_input and user_input1:
        input1 = user_room_input
        input_list = f'{user_input4} {user_input5} {user_input1} {user_input2} {user_input3} {user_input6}'
        # input_list.append(user_input2)
        # input_list.append(user_input3)
        # input_list.append(user_input4)
        # input_list.append(user_input5)
        # input_list.append(user_input6)
        # input_list.append(user_input7)
        # input_list.append(user_input8)
        # input_list.append(user_input9)
        # input_list.append(user_input10)

        result = main(input_list, input1)

    return render(request, 'request_page.html', {'result': result})
