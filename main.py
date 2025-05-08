import random
n = random.randint(1, 100)

a = -1
guesses = 0
while (a != n):
    a = int(input("Guess the number please: "))
    guesses += 1

    if (a > n):
        print("Lower number please")
    else:
        print("Higher number please")    

print(f"The guessed the number {n} correctly in {guesses} attempts.")