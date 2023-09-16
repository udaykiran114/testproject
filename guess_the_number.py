import random


random_number = int(random.random()*100)

max_number_of_attempts = 10

for i in range(max_number_of_attempts):
    guessed_number = int(input("Enter the number: "))
    if random_number==guessed_number:
        print("Correct Guess!")
        break
    elif random_number>guessed_number:
        print("Guessed number is too low!")
    elif random_number<guessed_number:
        print("Guessed number is too high!")
