password = ""

while password != "python123":
    password = input("Enter password: ")
    if password != "python123":
        print("Wrong password, try again.")

print("Access granted!")