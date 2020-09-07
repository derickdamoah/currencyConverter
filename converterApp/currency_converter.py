import requests
import sys
import pprint

try:
    amount_to_convert = float(input("Type Your Amount Here: "))
except:
    print("Please type an amount in DIGITS eg. 200")
    try:
        amount_to_convert = float(input("Type Your Amount Here: "))
    except:
        print("Please Try Again")
        sys.exit()

while True:
    convert_from= input("Covert From: ")
    convert_to = input("Convert To: ")
    if convert_from.isupper() and convert_to.isupper():
        break
    else:
        print("Please type the currency code in Capital Letters eg. 'USD'")


while len(convert_from) != 3 or len(convert_to) != 3:
    print("The Currency code CANNOT be longer than 3 digits, Please Try Again")
    convert_from = input("Covert From: ")
    convert_to = input("Convert To: ")

api_url = "https://api.exchangeratesapi.io/latest"
open_url = requests.get(api_url)
json_from_url = open_url.json()
#pprint.pprint(json_from_url)

if convert_from!= "EUR" and convert_to != "EUR":
    while (convert_from not in json_from_url["rates"].keys()) or (convert_to not in json_from_url["rates"].keys()):
        print("We cannot convert from this currency, Please Try a Different Currency")
        convert_from = input("Covert From: ")
        convert_to = input("Convert To: ")

open_url = requests.get(api_url+"?base="+convert_from)
json_from_url = open_url.json()

converted_amount = round(amount_to_convert * json_from_url["rates"][convert_to],2)

print(str(amount_to_convert), convert_from + " is equal to",
      converted_amount, convert_to)