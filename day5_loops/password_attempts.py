correct_password = "Python123"
for attempt in range(3):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Access Denied")