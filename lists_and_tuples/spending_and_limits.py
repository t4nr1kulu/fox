spendings=[]

while True:
    amount=input("Enter your spending amount(q to quit)")
    if amount.lower()=="q":
        print("quiting..")
        break
    amount=int(amount)
    if amount < 0:
        print("Amount can't be negative")
    else:
        spendings.append(amount)

high_spends=[]
total=0
aver=0
num=0
for spending in spendings:
    if spending>200:
        high_spends.append(spending)
    total+=spending
    num+=1
    aver=total/num

highest_number=spendings[0]
for n in spendings:
    if highest_number<n:
        highest_number=n

print(f"Total spending: {total}")
print(f"Average spending: {aver}")
print(f"The highest spending: {highest_number}")
print(f"High spends(200+): {high_spends}")