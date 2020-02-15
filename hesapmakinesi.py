secenek="""
        [1] Toplama [2] Çıkarma [3] Çarpma [4] Bölme [5] Üs Alma

"""
print(secenek)
secenek=int(input("Seçiminizi yapın: "))
sayi=input("İşlem yapılacak sayıları giriniz: ")
sayi_bölü=sayi.split(" ")

if secenek ==1:
    ilk_sayi=float(sayi_bölü[0])
    ikinci_sayi=float(sayi_bölü[1])

    print("{} + {} = {}".format(ilk_sayi,ikinci_sayi,ilk_sayi+ikinci_sayi))

elif secenek ==2:
    ilk_sayi = float(sayi_bölü[0])
    ikinci_sayi = float(sayi_bölü[1])
    print("{} - {} = {}".format(ilk_sayi,ikinci_sayi,ilk_sayi-ikinci_sayi))


elif secenek ==3:
    ilk_sayi = float(sayi_bölü[0])
    ikinci_sayi = float(sayi_bölü[1])
    print("{} * {} = {}".format(ilk_sayi,ikinci_sayi,ilk_sayi*ikinci_sayi))


elif secenek ==4:
    ilk_sayi = float(sayi_bölü[0])
    ikinci_sayi = float(sayi_bölü[1])
    print("{} / {} = {}".format(ilk_sayi,ikinci_sayi,ilk_sayi/ikinci_sayi))


elif secenek ==5:
    ilk_sayi = float(sayi_bölü[0]) #taban
    ikinci_sayi = int(sayi_bölü[1]) #üs
    print("{} ** {} = {}".format(ilk_sayi,ikinci_sayi,ilk_sayi**ikinci_sayi))


else:
    print("Hatalı Seçim Yaptınız!")