while True:
    number = input("Enter your even number or q to quit: ")
    if number.lower() == "q":
        print("exiting..")
    else:
        number=int(number)
        if number % 2==1:
            print("this is not a even number please try again.")
            continue
        if number % 2!=1:
            even=number**2
            print(f"your numbers square = {even}")
