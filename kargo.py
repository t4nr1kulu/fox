def cargo_calculation(weight,range):
    total = 50

    if weight > 5:
        total += (weight - 5)*10
    if range > 100:
        total += (range-100)*2
    return total


while True:
    weight=input("Enter your cargo weight(q ro exit): ")
    
    if weight.lower()=="q":
        print("exiting...")
        break
    miles = input("Enter your cargo range(q to exit): ")
    
    if miles.lower() == "q":
        print("exiting..")

    else:
        weight = int(weight)
        miles = int(miles)

        total = cargo_calculation(weight,miles)

        print(f"your total : {total}")
        


