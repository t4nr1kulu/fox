while True:
    password=len(input("set a password: "))
    if password < 8:
        print("your password lenght is to short is must be at least 8")
    else:
        print("your password set")
        break