import phonenumbers
import opencage
from phonenumbers import geocoder

print("[1]Пробив по номеру")
print("[2]Пробив по айпи") 
print("[3]Пробив по паспорту")
print("[4]Мануал по доксу")
print("[5]Настройки")
print("[6]Выход")

vvod = input("Выберите метод: ")


if vvod == "1":
  pnmr = phonenumbers.parse(input("Введите номер: "))

if vvod == "2":
  print("В разработке")
  exit("Выход...")

if vvod == "3":
  print("В разработке")
  exit("Выход...")

if vvod == "4":
	print("Всем привет! Я - sozdatelispython и сегодня я подробно обьясню, как научиться доксить используя ум и телеграмм ботов зная только номер, для начала мы переходим в бот @gtasearchbot123_bot и там мы вводим номер жертвы, допустим мы узнали город и возможное ФИО, далее мы должны перейти в бота @ubostrbot и там мы должны ввести полученную информацию в таком формате: Зайцев Тимофей, Красноярск, мы узнали почту и убедились что имя совпадает, также мы можем проверить соцсети но номеру и там мы можем узнать настоящее имя, лицо, дату рождения, итак мы пробили жертву но остались родители, по отчеству жертвы мы узнаем фамилию отца, вводим эти данные в Юзербокс: Зайцев Дмитрий, Красноярск, мы получили html страницу, открываем ее и с помощью кнопки поиска пишем ключевые слова, например ФИ и город где живет отец, полученные данные мы вводим в юзербокс: Зайцев Дмитрий Олегович,12.12.1997, Красноярск, мы получаем точный адрес, и другую информацию про отца")
	exit("Выход...")

if vvod == "5":
	print("РАСШИРЕННЫЙ ПОИСК - ОТКЛ")
	a = input("Введите да чтобы включить расширенный поиск: ")
	if a == "нет":
		exit("Выход...")
	if a == "да":
		print("Чтобы включить расширенный поиск перейдите в OSearch.py в проводнике и в последней строчке уберите хештег - #")
		exit("Выход...")
	else:
		print("Я не понял что вы написали")
		exit("Выход...")

if vvod == "6":
  exit("Выход...")

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

#print(result)