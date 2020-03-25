#Corona Tespit Kiti

while True:
    print("*********Aşağıdaki semptomları (Var/Yok) şeklinde yanıtlayınız!!!*********")
    secim1 = input("Yüksek ateş:")
    secim2 = input("Kuru öksürük:")
    secim3 = input("Nefes Alırken Zorlanma:")



    if secim1 =="var" and secim2 =="var" and secim3 =="var": #üç semptom
        print("En yakın sağlık kurumuna online başvuru yapınız riskiniz yüksek!")
    elif  secim1 =="var" and secim2 =="var" and secim3 =="yok": #ateş-öksür
        print("Evde kendinizi izole ediniz.sempotomlar var!")
    elif  secim1 =="var" and secim2 =="yok" and secim3 =="yok": # sadece ateş
        print("Sağlığınıza dikkat ediniz! Şuan için tek semptom var.")
    elif  secim1 =="yok" and secim2 =="yok" and secim3 =="yok": #belirti yok
        print("Maşallah turp gibisiniz :)")

    elif  secim1 =="yok" and secim2 =="yok" and secim3 =="var": #zorlanma
        print("Nefes antrenmanı şart")
    elif  secim1 =="yok" and secim2 =="var" and secim3 =="yok": #kuru
        print("Sigaradan uzak dur!")
    elif  secim1 =="var" and secim2 =="yok" and secim3 =="var": #ateş-nefes
        print("En yakın kuruluşa online randevu!")
    elif secim1 == "yok" and secim2 == "var" and secim3 == "var":
        print("Sigaraı bırak!! Eğer kullanmıyorsan En yakın kuruluşa online başvur!")
    else:
        print("Hatalı işlem!!!")