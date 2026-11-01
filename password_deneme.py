pasword = "admin123"
hak=3
for i in range(hak+1):
    enter=input("Şifrenizi girin: ")
    if enter!= "admin123":
        hak-=1
        if hak == 0:
            print("hesabınız bloke edildi")
            break
        print(f"hatalı şifre hakkınız {hak}")
    elif enter == "admin123":
            print("başarılı şifre")
            break
