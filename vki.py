#Vücut Kitle İndeksi Hesaplayan Program
import time


def indekHesap():
    try:
        print("******Vücut Kitle İndeksi Hesaplama******")
        time.sleep(1)
        print("~~~~Kilonuzu Giriniz!~~~~")
        kilo = float(input("-->Kilonuzu Giriniz:"))
        time.sleep(1)
        print("~~~Boyunuzu Giriniz!~~~\n--Örnek:1.79--")
        boy = float(input("-->Boyunuzu Giriniz:"))
        time.sleep(1)

        sonuc = kilo / (boy*boy)
        print("-->Sonucunuz:",sonuc)

        input("Devam etmek için bir tuşa bas!")
    except ValueError:
        time.sleep(1)
        print("-->Lütfen Sayı Giriniz!<--")

def sonucDegerlendirme():
    try:
        sonuc_gir = float(input("-->Sonucunuzu Giriniz:"))

        if sonuc_gir < 19 :
            time.sleep(1)
            print("Ciddi zayıflık.Kitle beden indeksiniz düşük!")
            input("Devam etmek için bir tuşa basınız.")

        elif sonuc_gir < 30:
            time.sleep(1)
            print("Kitle beden indeksiniz normal.")
            input("Devam etmek için bir tuşa basınız.")

        elif sonuc_gir > 30:
            time.sleep(1)
            print("Obezite belirtisi!")
            input("Devam etmek için bir tuşa basınız.")

    except ValueError:
        time.sleep(1)
        print("-->Lütfen Sayı Giriniz!<--")


while True:
    print("""
  ************************************
  *  [1]Vücut Kitle İndeksi Hesapla  *
  *  [2]Sonucuna Göre Değerlendirme  *
  *  [H]Hakkımızda                   *
  *  [Q]Çıkış                        *
  ************************************
    """)

    menu = input("Seçiminizi Yapınız:")

    if menu == "q":
        quit()

    elif menu == "1":
        indekHesap()

    elif menu == "2":
        sonucDegerlendirme()

    elif menu == "h":
        time.sleep(1)
        print("Bu uygulama Furkan Turgut tarafından geliştirilmiştir.\nEğitim amaçlı basit seviyede kodlanmıştır.")


