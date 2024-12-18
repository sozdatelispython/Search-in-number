import phonenumbers
import opencage
from phonenumbers import geocoder

print("[1]Пробив по номеру")
print("[2]Пробив по айпи") 
print("[3]Пробив по паспорту")
print("[4]Выход")

vodka = input("Выберите метод: ")


if vodka == "1":
  pnmr = phonenumbers.parse(input("Введите номер: "))

if vodka == "2":
  print("В разработке")
  exit(1)

if vodka == "3":
  print("В разработке")
  exit(1)

if vodka == "4":
  exit(1)

locat = geocoder.description_for_number(pnmr, 'ru')
print(f"Страна: {locat}")

from phonenumbers import carrier
print(f"Моб.Оператор: {carrier.name_for_number(pnmr, 'ru')}")

from opencage.geocoder import OpenCageGeocode

key = '9e76fbd7ccdf4f2abf07787eaef3c49f'

geocoder = OpenCageGeocode(key)
query = str(locat)
result = geocoder.geocode(query)

lat = result [0] ['geometry'] ['lat']
lng = result [0] ['geometry'] ['lng']

print(f"Ширина & Долгота: {lat}, {lng}")

#ЧТОБЫ БЫЛ РАСШИРЕННЫЙ ПОИСК ПОСЛЕ ЭТОЙ СТРОКИ НУЖНО ВВЕСТИ print("result")