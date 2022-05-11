import string
import random
from turtle import end_fill

litery = list(string.ascii_letters)
cyfry = list(string.digits)
znaki_specjalne = list("!@#$%^&*()")
znaki = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
    dlugosc = int(input("Podaj dlugosc hasla: "))

    litery_ilosc = int(input("Podaj liczbe liter w hasle: "))
    cyfry_ilosc = int(input("Podaj liczbe cyfr w hasle: "))
    znaki_specjalne_ilosc = int(input("Podaj liczbe znakow specjalnych w hasle: "))

    znaki_ilosc = litery_ilosc + cyfry_ilosc + znaki_specjalne_ilosc

    if znaki_ilosc > dlugosc:
        print("Liczba znakow jest wieksza od dlugosci hasla")
        return

    password = []

    for i in range(litery_ilosc):
        password.append(random.choice(litery))
    
    for i in range(cyfry_ilosc):
        password.append(random.choice(cyfry))

    for i in range(znaki_specjalne_ilosc):
        password.append(random.choice(znaki_specjalne))

    if znaki_ilosc < dlugosc:
        random.shuffle(znaki)
        for i in range(dlugosc - znaki_ilosc):
            password.append(random.choice(znaki))

    random.shuffle(password)

    print("".join(password))


generate_random_password()