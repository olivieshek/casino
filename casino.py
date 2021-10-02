"""
TODO:
	игра в казино - MAIN
	кухня
	сон
	болтовня

"""
import random

def casino():
	print("Сыграть или поболтать с кем-нибудь?")
	print('''	1 - сыграть
	2 - поболтать''')
	user_choice = 0
	while user_choice not in ("1", "2"):
		user_choice = input("Выберите число: ")
	if user_choice == "1":
		print("сыграем")
	else:
		print("Вы подошли к какому-то человеку.")
		person = random.randrange(1, 4)
		if person == 1:
			print("Вы подошли к девушке в красном спортивном костюме.")
			print("- Что надо?")
			print("Что ответить?")
			print('''	1 - "Вы не соблюдаете дресс-код!"
	2 - извиниться и уйти
	3 - попытаться познакомиться''')
			ans = 0
			while ans not in ("1", "2", "3"):
				ans = input("Введите число: ")
			if ans == "1":
				print("- Я вообще-то тут работаю!")
			elif ans == "2":
				print("- Ну и иди. Только и умеете под ногами путаться!")
			else:
				print("- Я вообще-то тут работаю! Мне не до болтовни!")
		elif person == 2:
			pass
		elif person == 3:
			pass
		else:
			pass
		casino()

def home():
	print("Вы сидите дома")
	print("Куда пойти?")
	print('''	1 - в казино
	2 - на кухню
	3 - спать''')
	user_choice = 0
	while user_choice not in ("1", "2", "3"):
		user_choice = 0
		user_choice = input("Введите число: ")
	if user_choice == "1":
		print("Вы в казино.")
		casino()
	elif user_choice == "2":
		print("на кухне")
	else:
		print("спите")
home()
