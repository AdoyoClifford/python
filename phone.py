import phonenumbers

#import geocoder
from phonenumbers import geocoder

a = input('Enter the phone number: ')

phonenumber = phonenumbers.parse(a)
print(geocoder.country_name_for_number(phonenumber, "en"))