tek_sayac = 0
cift_sayac = 0

for i in range(4):
    sayi = int(input("Sipariş numarasını girin: "))
    
    if sayi % 2 == 1:
        tek_sayac += 1
    else:
        cift_sayac += 1

print(f"Toplam Tek: {tek_sayac} | Toplam Çift: {cift_sayac}")