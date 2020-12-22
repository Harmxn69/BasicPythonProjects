import random
 
hidden = random.randrange(1, 10)
# print hidden
 
guess = int(input("Please enter your guess: "))
 
if guess == hidden:
    print ("You got it!")
elif guess < hidden:
    print ("Your guess is too low")
else:
    print("Your guess is too high")