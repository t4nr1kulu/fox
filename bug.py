def bonus_hesapla(satis):
    bonus = (satis * 0.10)+satis
    return bonus

while True:
    satis_miktari = input("Satış miktarını girin (Çıkış: q): ")

    if satis_miktari == "q":
        print("Çıkılıyor...")
        break
    satis_miktari=int(satis_miktari)
    if bonus_hesapla(satis_miktari) >= 1000:
        print("Mükemmel satış!!")
    elif bonus_hesapla(satis_miktari) >= 500:
        print("Tebrikler, iyi iş!")
    else:
        print("Daha çok satmalısın.")