import random

sayi = random.randint(1,20)
hak = 5
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin= int(input("Tahmin:"))

    if sayi == tahmin:
        print("Tebrikler {}. defada bildiniz.".format(sayac))
        break
    elif sayi > tahmin:
        print("Yukarı!")
    else:
        print("Aşağı")

    if hak == 0:
        print("Hakkınız bitti. Tutulan sayi {}".format(sayi))
