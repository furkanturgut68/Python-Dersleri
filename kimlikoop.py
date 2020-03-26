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
