bal = float(input("enter your balance: "))

while True:
    password = input("enter yoru password: ")

    if password != "1903":
        print("wrong password")
        continue
    while True:
        select = input("choose your destinitaion 1,2,3: ")
        if select == "1":
            print(f"Your balance = {bal}")
        elif select == "2":
            minus = float(input("How much do you want =>"))
            if minus > bal:
                print("Negative balance")
                continue
            bal-=minus
            print(bal)
        else:
            print("exiting to pin page")
            break