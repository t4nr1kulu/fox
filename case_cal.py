def average(toplam,day):
    aver=toplam/day
    return aver

total=0

for i in range(1,6):
    ciro = float(input("enter your ciro"))
    total += ciro
    
print(average(total,5))



