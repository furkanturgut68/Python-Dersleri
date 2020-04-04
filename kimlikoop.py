class Kimlik:
    def __init__(self,isim,soyad,dogumYili,memleket):
        self.isim = isim
        self.soyad = soyad
        self.dogumYili = dogumYili
        self.memleket = memleket

    def isimDegis(self,isim):
        self.isim = isim

    def __str__(self):
        return ("İsim:{} Soyisim:{} Doğum Yılı:{} Memleket:{}".format(self.isim,self.soyad,self.dogumYili,self.memleket))

class Ehliyet(Kimlik):
    def __init__(self,isim,soyad,dogumYili,memleket,ehliyetNo,aldigiYil):
        Kimlik.__init__(self,isim,soyad,dogumYili,memleket)
        self.ehliyetNo = ehliyetNo
        self.aldigiYil = aldigiYil

    def __str__(self):
        return ("İsim:{} Soyisim:{} Doğum Yılı:{} Memleket:{} Ehliyet No:{} Aldığı Yıl:{}".format(self.isim,self.soyad,self.dogumYili,self.memleket,self.ehliyetNo,self.aldigiYil))




c1 = Ehliyet("Furkan","Turgut",2001,"Aksaray",1656,2021)
print(c1)

k1 = Kimlik("Furkan","Turgut",2001,"Aksaray")
print(k1)

print( """
[1]Kimlik Detaylı Görüntüle
***************************
[a]Kimlik Numarası
[b]İsim
[c]Soyisim
[d]Doğum Yılı
[e]Memleket

[2]Ehliyet Detaylı Görüntüle
****************************
[f]Ehliyet Numarası
[g]Aldığı Yıl
""")
while True:
    os.system("cls")
    mainmenü =(input("Seçinizi Giriniz:"))

    if mainmenü =="1":
        print(kimlik)
        time.sleep(3)
    elif mainmenü =="a" :
        print(" T.C Kimlik Numarası:",kimlik.tcNo)
        time.sleep(3)
    elif mainmenü =="b":
        print("İsim:",kimlik.isim)
        time.sleep(3)
    elif mainmenü =="c":
        print("Soyad:",kimlik.soyad)
        time.sleep(3)
    elif mainmenü =="d":
        print("Doğum Yılı:",kimlik.dogumYili)
        time.sleep(3)
    elif mainmenü =="e":
        print("Memleket:",kimlik.memleket)
        time.sleep(3)
    elif mainmenü =="2":
        print(ehliyet)
        time.sleep(3)
    elif mainmenü =="f":
        print("Ehliyet Numarası:",ehliyet.ehliyetNo)
        time.sleep(3)
    elif mainmenü =="g":
        print("Aldığı Yıl:",ehliyet.aldigiYil)
        time.sleep(3)
    else:
        print("Hatalı Giriş!!!\nLütfen menüye göre seçim yapınız!")
