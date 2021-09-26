import random
number = random.randint(1,9)
chances = 5
guess = input("enter your guess: ")
print(guess)
while chances <5:
    if guess == number:
        print("Congrats, you win")
        break
    elif guess<number:
        print("you were too low, guess a number higher than",guess)
    elif guess>number:
        print("you were too high, guess a number lower than",guess)
    chances = chances-1
if not chances <5:
    print("you lose, the number was:",number)
