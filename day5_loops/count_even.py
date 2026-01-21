number = int(input("Enter a number: "))
count = 0
for i in range(1, number +1):
    if i % 2 ==0:
        count +=1
print("Even numbers count:", count)