def mesai_hesapla(toplam_saat):
    ucret = toplam_saat * 100
    return ucret

hour=4
kasa = 0

for gun in range(1,hour):
    saat = int(input(f"{gun}. gün mesai saatini girin: "))
    kasa += saat

print(f"Toplam ödenecek tutar: {mesai_hesapla(kasa)} TL")