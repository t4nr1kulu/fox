fluid=100
flint=3

while True:
    lighther = input("çakmak için c ye benzin yenilemek için b ye taş yenilemek için t ye çıkmak için q ya basın")

    if lighther.lower() == "q":
        print("çıkış yapıldı")
        break

    elif lighther.lower() == "c":
        if fluid == 0:
            print("Benzin bitti çakamazsın")
        elif flint == 0:
            print("Taş bitti çakamazsın")
        else:
            print("Ateş Var")
            fluid-=20
            flint-=1

    elif lighther.lower() == "b":
        if fluid == 100:
            print("Benzin Full")
            continue
        print("Benzin Yenilendi")
        fluid = 100

    elif lighther.lower() == "t":
        if flint == 3:
            print("Taş full")
            continue
        print("Taş yenilendi")
        flint = 3
        continue
    else:
        print("Geçersiz komut, lütfen geçerli bir harf girin.")


    


