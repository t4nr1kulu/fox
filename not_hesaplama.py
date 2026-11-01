def not_hesapla(vize,final):
    average=(vize * 0.6)+(final * 0.4)
    return average



while True:
    vize = input("Vize notu giriniz(q to exit): ")
    if vize.lower() =="q":
        print("exiting")
        break
    final = input("Final notu giriniz(q to exit): ")
    if final.lower() =="q":
            print("exiting")
            break

    
    else:
        vize=int(vize)
        final=int(final)

        ortalama = not_hesapla(vize,final)

        if not_hesapla(vize,final) >= 90:
            print(f"A notunuz{ortalama}")
        elif not_hesapla(vize,final)>=70:
            print(f"B notunuz{ortalama}")
        elif not_hesapla(vize,final)>=50:
            print(f"C notunuz {ortalama}")
        else:
            print(f"daha çok çalışman lazım {not_hesapla(vize,final)}")
            
