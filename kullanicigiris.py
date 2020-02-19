#Kullanıcı Giriş Uygulaması (Deneme)

kullanici="furkanturgut"
sifre="python"

while (True):
    defkullanici=input("Kullanıcı Adını Giriniz: ")
    defsifre=input("Lütfen Şifrenizi Giriniz: ")

    if ((kullanici==defkullanici) and (sifre==defsifre)):
        print("İşlem başarılı!",kullanici)
        break
    elif ((kullanici !=defkullanici) and (sifre==defsifre)):
        print("Kullanıcı Adı Hatalı!")
    elif ((kullanici==defkullanici) and (sifre!= defsifre)):
        print("Şifre Hatalı!")
    else:
        print("Hatalı İşlem Yaptınız!!1")


