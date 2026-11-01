def bilet_otomasyonu(): 
    
    while True:
        secim = input("Menü seçin 1,2,3 çıkmak için q: ")

        if secim=="q":
            print("çıkılıyor")
            break

        elif secim=="1":
            bilet=input("Kaç bilet istersininiz (çıkış için q): ")
            if bilet.lower() =="q":
                print("çıkılıyor")
                continue
            else:
                bilet=int(bilet)
                for i in range(1,bilet+1):
                    print(f"Bilet numarası {i}: yazdırıldı")

        elif secim=="2":
            while True:
                sifre=input("Şifre girin(çıkış için q): ")
                if sifre.lower() =="q":
                    print("ana medüye dönülüyor")
                    break
                elif sifre == "admin123":
                    print("Doğru şifre girdiniz")
                    break
                else:
                    print("yanlış şıfre")
                
                
        elif secim=="3":
            print("kapatılıyot!!!!")
            break

bilet_otomasyonu()
