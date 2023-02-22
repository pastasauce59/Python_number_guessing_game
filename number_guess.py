from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

numbers = []
for n in range(1, 101):
    numbers.append(n)

print("I'm thinking of a number between 1 and 100.")
number =  random.choice(numbers)

#FOR TESTING
print(f"psst, the number is {number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attemps = 10
else:
    attemps = 5

while attemps != 0:
    print(f"You have {attemps} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))
    # if guess > number:
    #     print("Too high.")
    #     attemps -= 1
    #     if attemps == 0:
    #         print("You've run out of guesses, you lose.")
    #     else:
    #         print("Guess again.")
    # elif guess < number:
    #     print("Too low.")
    #     attemps -= 1
    #     if attemps == 0:
    #         print("You've run out of guesses, you lose.")
    #     else:
    #         print("Guess again.")
    # elif guess == number:
    #     print(f"You got it!. The answer was {number}.")
    #     attemps = 0

    if guess != number:
        attemps -= 1
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        elif guess == number:
            print(f"You got it!. The answer was {number}.")
            attemps = 0
        
        if attemps != 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")