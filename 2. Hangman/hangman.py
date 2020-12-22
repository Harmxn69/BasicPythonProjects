from randomwords import list_of_words
import random
import time


print("Start guessing...")

time.sleep(0.5)


word = random.choice(list_of_words)

guesses = ''
turns = 10

while turns > 0:         
    failed = 0              
    for char in word:      
        if char in guesses:    
            print(char),    

        else:
            print("-"),
            failed += 1 

    if failed == 0:        
        print(" ")
        print("You won")
        print("-------------------------------") 
        print(" ")
        break              

    print

    guess = input("Make a guess:   ") 
    guesses += guess                    

    if guess not in word:  
        turns -= 1        
        print("Wrong") 
        print ("You have", + turns, 'more guesses') 

        if turns == 0: 
            print(" ")
            print("You lost, the words was " + word) 
            print("-------------------------------") 
            print(" ")
