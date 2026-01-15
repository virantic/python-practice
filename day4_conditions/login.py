correct_username = "ryannut"
correct_password = "456987"

username = input("what is your username? ")
password = input("What is your password?")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid credentials")