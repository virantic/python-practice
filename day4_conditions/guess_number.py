secret_num = 10
guess = int(input("Guess the secret number: "))

if guess == secret_num:
    print("Correct!")
elif guess > secret_num:
    print("Too high")
else:
    print("Too low")