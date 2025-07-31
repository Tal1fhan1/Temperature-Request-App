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
    
    user_room_input = 'ee47fba3-b715-434e-ba78-d7b962483e8c'
    user_input1 = '88fd4933-05fe-45e7-84b5-4322be461065'
    user_input2 = 'cb95f408-a1f6-4faa-8d4a-b7ffb64465e3'
    user_input3 = '293ead57-750f-4762-8548-a2c29acf4acc'
    user_input4 = 'bbaafef6-02f7-446e-84e2-42d9f9459b3d'
    user_input5 = '78b6c72c-e8e7-419f-b988-b574a147be13'
    user_input6 = 'b4564b30-7300-4692-adbe-606ebad52096'
    # user_input7 = '31b1aef9-657d-4d04-a7c0-d81944205620'
    # user_input8 = 'b7854ac1-650e-425b-b4c5-e9c9523c2331'
    # user_input9 = 'c89cf283-8368-4225-8642-c436c33d0052'
    # user_input10 = '24c18b89-34c6-4b60-b9e6-8a9577a04feb'

    
    result = None

    if user_room_input and user_input1:
        input1 = user_room_input
        input_list = f'{user_input1} {user_input2} {user_input4}'
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
