def discount(price):
    price=price-(price*0.2)
    return price


total = 0
for i in range(3):
    price=int(input("Enter your goods price: "))
    price=discount(price)
    total+=price

print(f"your sub total> {total}")
    