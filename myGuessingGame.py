
# Import built-in module for generating (random) number
import random

# Prompt, store, and print user name as `user`
user = input("Hello, there. Enter your name to begin... ")
print("Alright, {}!".format(user))
print("I'm thinking of a number between 1 and 10")

# Generate random integer and store as `num`
number = random.randint(1, 10)
# Initialize `number_of_guesses` for counting tries (guesses)
number_of_guesses = 0

while number_of_guesses < 10:
    guess = int(input("Take a guess: "))
    number_of_guesses += 1
    if guess < number:
        print("Shucks, your number is too low.")
    if guess > number:
        print("Rats! Your number is too high.")
    if guess == number:
        print("You guessed the number")
        print("{} gets a gold star." .format(user))
        break
