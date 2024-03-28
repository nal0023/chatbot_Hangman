import time
import sys
import random


#introduction Diologue
print("welcome to Hangman!")

name = input("What is your name Challenger?")

answer = int(input("Welcome"+name+ ", are you ready test your Hangman skills? Choose 1 for yes or 0 for no!"))

if answer == 1:
    
    print("Alright, Let's...")

    time.sleep(1)

    print("Play...")

    time.sleep(1)

    print("HANGMAN!!!")

elif answer == 0:

    print("Too bad your being forced to play anyway!")

    time.sleep(1)

    print("Now Let's...")

    time.sleep(1)

    print("Play...")

    time.sleep(1)

    print("HANGMAN!!!")

else:

    print("What are you doing you goof I only gave you two options, so choose one of them.")

    time.sleep(1)

    print("Actually, I'm gonna force you to play!!!")

    print("Let's...")

    time.sleep(1)

    print("Play...")

    time.sleep(1)

    print("HANGMAN!!!")
    

listOfWords = ("words", "apple", "cough", "thumbscrew", "phlegm", "yachtsman", "espionage", "stymied", "Explosion", "Earth", "schnapps", "curacao", "ivory", "Quartz", "morgantown", "triphthong", "matrix", "err") 

word = random.choice(listOfWords)

time.sleep(2)

print("Now here's the hidden word, take a guess and see if your right. REMEMBER!!! You only get 10 chanes!")

guess = ''

tries = 10

# This while loop determines if the player input is correct and counts the number of tries the player has left.
while tries > 0:

    #Player amount of incorrect guesses
    fails = 0

    #For loop to see if player guess is within the word
    for char in word:

        if char in guess:

            print(char)

        else:

            print("_")

            #Wrong guess, # of fails increases by 1
            fails += 1
            
    if fails == 0:
        print("You Win")
    
        print("The word is: ",word)
        break

    guesses = input("guess a character:")
     
    guess += guesses

    #For loop for lowering the value of tries by 1, when player incorrectly guesses
    if guesses not in word:
         
        tries -= 1
     
        print("Wrong")
         
        print("You have", + tries, 'more guesses')
         
         
        if tries == 0:
            print("You Loose")

            print("The word was: ",word)
