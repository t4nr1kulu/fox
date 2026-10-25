master_tone= 0

while True:
    e_tone = input("Ton giriniz(q to quit):")

    if e_tone.lower() =="q":
        print("çıkış yapıldı")
        break
    e_tone = int(e_tone)
    master_tone += e_tone
    if master_tone < 15:
        print(f"Yetersiz ton{master_tone}")
        
    elif master_tone>15:
        print(f"Ton çamurlaştı{master_tone}")
        n_tone=input(f"Ton çamurlaştı düşürmek ister misin(q to quit):{master_tone}")
        if n_tone.lower()=="q":
            print("çıkış yapıldı")
            break
        n_tone = int(n_tone)
        master_tone-=n_tone

    if master_tone == 15:
        print(f"Kıvamında{master_tone}")
        break
        