import phonenumbers
from test import num

from phonenumbers import geocoder
ch_num = phonenumbers.parse(num,"CH")
print(geocoder.description_for_number(ch_num, "en"))

from phonenumbers import carrier
serv_num = phonenumbers.parse(num ,"RO")
print(carrier.name_for_number(serv_num,"en"))