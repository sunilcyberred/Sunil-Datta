GNU nano 8.7                                                      sunil.py
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type
from colorama import Fore, Style, init

init(autoreset=True)

def banner():
    print(Fore.GREEN)
    print("===================================")
    print("        PHONE OSINT TOOL")
    print("        Author: Sunil Dutta")
    print("===================================")
    print(Style.RESET_ALL)

def number_info():
    number = input("Enter phone number with country code: ")

    try:
        phone = phonenumbers.parse(number)

        valid = phonenumbers.is_valid_number(phone)
        country = geocoder.description_for_number(phone, "en")
        carr = carrier.name_for_number(phone, "en")
        tz = timezone.time_zones_for_number(phone)
        ntype = number_type(phone)

        if ntype == 1:
            type_name = "Mobile"
        else:
            type_name = "Unknown"

        print("\nResult")
        print("Valid:", valid)
        print("Country:", country)
        print("Carrier:", carr)
        print("Timezone:", tz)
        print("Type:", type_name)

    except:
        print("Invalid number format")

def osint_links():
    number = input("Enter phone number with country code: ")
    num = number.replace("+","")

    print("\nOSINT Links")

    print("Google Search")
    print("https://www.google.com/search?q=" + num)

    print("\nTruecaller Search")
    print("https://www.truecaller.com/search/in/" + num)

    print("\nWhatsApp Chat")
    print("https://wa.me/" + num)

    print("\nFacebook Search")
    print("https://www.facebook.com/search/top?q=" + num)

    print("\nTwitter Search")
    print("https://twitter.com/search?q=" + num)

    print("\nTelegram Link")
    print("https://t.me/" + num)

def menu():
    print("\nSelect Option")
    print("1 Number Intelligence")
    print("2 OSINT Search Links")
    print("3 Exit")

while True:
    banner()