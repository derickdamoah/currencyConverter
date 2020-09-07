from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    return render(request, "home.html",)

def convert(request):
    amount = float(request.POST['amount'])
    convert_from = request.POST['convertFrom']
    convert_to = request.POST['convertTo']
    if convert_from != convert_to:
        open_url = requests.get("https://api.exchangeratesapi.io/latest?base={}".format(convert_from))
        json_from_url = open_url.json()
        converted_amount = round(amount * json_from_url["rates"][convert_to], 2)
    else:
        converted_amount = amount*1

    return render(request, "result.html", {"amount": amount, "convertTo": convert_to, "convertFrom": convert_from, "result": converted_amount})



