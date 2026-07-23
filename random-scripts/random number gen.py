import random
random_number = int(input("Enter a random number: "))
number = random.randint(1, 69)
if (random_number == number):
    print("You guessed the number correctly!")
else:
    print(f"sorry you got it wrong the correct number was {number}")