password = "1234"

while True:
    entry = input("Enter your password or q to quit: ")
    if entry.lower()=="q":
        print("exiting")
        break
    else:
        if entry == "1234":
            print("your password correct")
            break
        else:
            print("Wrong password, try again.")
            continue

print("Login successful!")