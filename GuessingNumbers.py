import random
print("Number guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9):")
while chances < 5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulation !!! 🤴 YOU WON 🤴 !!!")
        break
    elif guess < number:
        print("Your guess was too low: Guess a number higher than yours", guess)

    
    else:
        print("Your guess was too high: Guess a number lower than yours", guess)
    chances += 1
if not chances < 3:
    print("YOU Lose 😖 The number is", number)