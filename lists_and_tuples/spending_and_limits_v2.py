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

if len(spendings)==0:
    print("No spending entered")
else:
    high_spends=[]
    total=0
    highest_number=spendings[0]

    for spending in spendings:
        if spending >= 200:
            high_spends.append(spending)
        if spending>highest_number:
            highest_number=spending
        total+=spending
    aver=total/len(spendings)



    print(f"Total spending: {total}")
    print(f"Average spending: {aver:.2f}")  
    print(f"The highest spending: {highest_number}")
    print(f"High spends (200+): {high_spends}")