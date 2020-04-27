class Circle:
    pi = 3.14

    def __init__(self,yaricap = 1):
        self.yaricap = yaricap

    #Method
    def cevreHesapla(self):
        return 2*self.pi + self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap**2)


c1 = Circle(2)

print("c1: alan= {} çevre={} ".format(c1.alanHesapla(),c1.cevreHesapla()))


