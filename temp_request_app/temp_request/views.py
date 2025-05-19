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
    
    user_room_input = request.GET.get('room_input', '')
    user_input1 = request.GET.get('input1', '')
    user_input2 = request.GET.get('input2', '')
    user_input3 = request.GET.get('input3', '')
    user_input4 = request.GET.get('input4', '')
    user_input5 = request.GET.get('input5', '')
    user_input6 = request.GET.get('input6', '')
    user_input7 = request.GET.get('input7', '')
    user_input8 = request.GET.get('input8', '')
    user_input9 = request.GET.get('input9', '')
    user_input10 = request.GET.get('input10', '')
    
    result = None

    if user_room_input and user_input1:
        input1 = user_room_input
        input_list.append(user_input1)
        input_list.append(user_input2)
        input_list.append(user_input3)
        input_list.append(user_input4)
        input_list.append(user_input5)
        input_list.append(user_input6)
        input_list.append(user_input7)
        input_list.append(user_input8)
        input_list.append(user_input9)
        input_list.append(user_input10)

        result = main(input_list, input1)

    return render(request, 'request_page.html', {'result': result})
