secenek=("""
     [1] Toplama
     [2] Çıkarma
     [3] Bölme  
        
        
""")
print(secenek)
secenek=int(input("İşlem yapılacak sayıyı giriniz: "))
sayi=input("sayı Gİr: ")
sayi_bölü=sayi.split(" ")

if secenek ==1:
    ilk_sayi=float(sayi_bölü[0])
    ikinci_sayi=float(sayi_bölü[1])
    print("{}+{}={}".format(ilk_sayi,ikinci_sayi,ilk_sayi+ikinci_sayi))

elif secenek ==2:
    ilk_sayi = float(sayi_bölü[0])
    ikinci_sayi = float(sayi_bölü[1])
    print("{}-{}={}".format(ilk_sayi, ikinci_sayi, ilk_sayi - ikinci_sayi))

elif secenek ==3:
    ilk_sayi = float(sayi_bölü[0])
    ikinci_sayi = float(sayi_bölü[1])
    print("{}/{}={}".format(ilk_sayi, ikinci_sayi, ilk_sayi / ikinci_sayi))


