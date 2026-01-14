a = 10
b = 3

print(a + b)
print(a % b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)


age = 15
print(age >= 15)
print(age <=20)
print(age ==19)
print(age !=15)


age = 20
citizen = True
print(age >=18 and citizen)
print(age ==17 or citizen)


age = int(input("Enter your age: "))
if age >=18:
    print("You are eligible to vote✅")
else:
    print("You are not eligible to vote🤧")