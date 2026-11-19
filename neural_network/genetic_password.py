# ============================================================
# Genetic Algorithm - Password Evolver
# Amaç: Rastgele karakter dizilerinden başlayıp seçilim,
# çaprazlama ve mutasyon yoluyla hedef şifreyi bulmak.
# ============================================================

import random

# --- Ayarlar (Parametreler) ---
# Hedef şifre, karakter havuzu ve her nesildeki birey sayısı
target="QUEENS OF THE STONEAGE"
chars="ABCDEFGHIJKLMNOPRSQTUVWXYZ "
population_size=1000

# --- 1. Popülasyon (Population) ---
# Hedef şifre uzunluğunda rastgele kelimeler üret
population=[]
for i in range(population_size):
    kelime=""
    for n in range(len(target)):
        kelime+=random.choice(chars)
    population.append(kelime)
print("First gen:",population)


# --- 2. Puanlama (Fitness) ---
# Her kelimenin hedef şifreyle kaç harfinin doğru yerde eşleştiğini hesapla



def calfitness(target,pop):
    scored_pop=[]
    for i in pop:
        score=0
        for n in range(len(target)):
            if i[n] == target[n]:
                score+=1
        fitness=score/len(target)
        scored_pop.append((i,fitness))
    return scored_pop


# --- 3. Çaprazlama ve Mutasyon (Crossover & Mutation) ---
# En yüksek puanlıları seç, parçalarını birleştir ve ufak harf değişiklikleri yap

def crossover(kelime1,kelime2):
    cut=random.randint(1,len(target)-1)
    return kelime1[:cut]+kelime2[cut:]

def mutation(kelime):
    yeni_kelime=""
    for harf in kelime:
        if random.random()<0.04:
            yeni_kelime += random.choice(chars)
        else:
            yeni_kelime += harf
    return yeni_kelime



# --- 4. Evrim Döngüsü (Evolution Loop) ---
# Hedef şifre bulunana kadar yukarıdaki adımları tekrar et 
generation=1
def puan_getir(x):
    return x[1]
while True:
    puanlilar=calfitness(target,population)
    sirali = sorted(puanlilar, key=puan_getir, reverse=True)
    print(sirali[0])
    if sirali[0][1] == 1.0:
        print(sirali[0][0], "şifre kırıldı")
        break
    en_iyiler = sirali[:population_size // 2]
    yeni_nesil=[]
    for i in range(population_size):
        ebeveyn1 = random.choice(en_iyiler)[0]
        ebeveyn2 = random.choice(en_iyiler)[0]
        kelime=crossover(ebeveyn1,ebeveyn2)
        kelime=mutation(kelime)
        yeni_nesil.append(kelime)
    population=yeni_nesil




