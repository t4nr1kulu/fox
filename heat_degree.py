toplam_sicaklik=0

while True:
    s_input=input("Sıcaklık değerini giriniz (çıkmak için q): ")

    if s_input.lower() == "q" :
        break
    s_input= int(s_input)
    toplam_sicaklik += s_input

    if toplam_sicaklik < 150:
        print("Yeterli ısıya ulaşmadı")
        continue
    else:
        print("Başarılı")
        break
    