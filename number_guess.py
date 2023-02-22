from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")

numbers = []
for n in range(1, 101):
    numbers.append(n)

print("I'm thinking of a number between 1 and 100.")
number =  random.choice(numbers)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attemps = 10
else:
    attemps = 5

while attemps != 0:
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        attemps -= 1
        print(f"You have {attemps} attemps remaining to guess the number")
    elif guess < number:
        print("Too low")
        attemps -= 1
        print(f"You have {attemps} attemps remaining to guess the number")
    elif guess == number:
        print("You got it!.")