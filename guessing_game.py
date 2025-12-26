import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎮 Welcome to the Guessing Game!")
print("🔎 Clue: The number is either ODD or EVEN")

if secret_number % 2 == 0:
    print("Hint: The number is EVEN")
else:
    print("Hint: The number is ODD")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        break
