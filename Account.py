import time
import os

kullanıcı="furkan"
sifre="123ft"
hesapNo="TR000011223344"


def AnaMenu():
    if kullanıcı == kullanıcıLogin and sifre == sifreLogin:

        print("""
                Sistemimize Hoşgeldiniz.
                Bu uygulama Furkan Turgut tarafından geliştirilmiştir.
                Saygılarla...
                cCc Komünizm cCc Bank                

                """)

    elif kullanıcıLogin == kullanıcı and sifreLogin != sifre:
        print("Şifre hatalı!")
        time.sleep(1)

    elif kullanıcıLogin != kullanıcı and sifreLogin == sifre:
        print("Kullanıcı adı hatalı!")
        time.sleep(2)
    elif kullanıcıLogin != kullanıcı and sifreLogin != sifre:
        print("Hatalı giriş yaptınız!")
        time.sleep(2)
    else:
        print("Hatalı İşlem!")
        time.sleep(2)
####################################
def İslemler():
    bakiye = 1656

    print("""
                    [1]Hesap Bilgilerini Görüntüle
                    [2]Bakiye İşlemleri

                    """)

    Giris =input("Seçiminizi yapınız:")

    if Giris =="1":
        print("""Kullanıcı Adı:{}
Şifre:{}
Hesap Numarası:{}
       
        """.format(kullanıcı,sifre,hesapNo))
        input("Devam etmek için bir tuşa basınız.")
        İslemler()

    elif Giris =="2":
        BakiyeIslem()
        İslemler()

        
def BakiyeIslem():

    print("""[1]Para Çekme
    [2]Para Yatırma    
    [3]Bakiye Sorgusu
    [Q]Ana menüye dönüş    
        
        """)
    bakiye = 1000

    while True:
        islem = input('İslem yapmak istediğiniz numarayı yazınız:')

        if (islem == "Q"):
            print("Programdan çıkılıyor")
            break
        elif islem =="1":
            miktar = int(input("Çekilecek miktarı giriniz:"))
            if (bakiye - miktar < 0):
                print("Yetersiz bakiye")

            else:
                bakiye = bakiye - miktar

                print("Hesabınızdan {} ₺ para çektiniz".format(miktar))

        elif islem =="2":
            yatacak = int(input('yatırmak istediğiniz miktarı girin'))
            bakiye = bakiye + yatacak
            print('Hesabınıza {} ₺ yatırdınız'.format(yatacak))


        elif islem == "3":
            print('Bakiyeniz {} ₺ dir'.format(bakiye))
        else:
            print('Geçersiz işlem')


os.system("cls")

print("cCc Komünizm cCc Bank'a Hoşgeldiniz")
kullanıcıLogin = input("Kullanıcı Adını Giriniz:")
sifreLogin = input("Şifrenizi Giriniz:")


while True:
    class GirisMesaj:
        AnaMenu()
        time.sleep(2)
    class Menuler(GirisMesaj):
        İslemler()

    break
