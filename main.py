from queue import Empty
from words import word
import random
import string

def pickWord(word):
    pick = random.choice(word)

    while ("-" or " ") in pick:
        pick = random.choice(word)

    return pick

def hangman():
    pick = pickWord(word).upper()
    wordLetters = set(pick) #contains the letters in pick -> set is unordered and cannot contain duplciates
    alphabet = set(string.ascii_uppercase)
    userLetters = set()
    
    life = 5
    
    while len(wordLetters) > 0 and life > 0:
        printWord(pick, userLetters)
        print("Number of lives: %d" % life)
        print("You have used the letters: " , " ".join(userLetters))
        user_input = input("Type a letter or type 'guess' to guess entire word: ").upper()
     
        if user_input == "GUESS":
            guess = input("Type your guess: ").upper()
            if guess == pick:
                 print("Wow! You guessed right!")
                 break
            else:
                print("Not quite -> lost a chance")
                life = life - 1
        elif user_input not in alphabet:
            print("\nInputs needs to be a character/letter or 'guess' -> Try again ")
        elif user_input in (alphabet - userLetters): #if the input is a letter that has not been inputted before
            userLetters.add(user_input)
            if user_input in wordLetters:
                wordLetters.remove(user_input)
                print("Bingo! One letter down")
            else:
                print("Invalid Character -> lost a chance")
                life = life - 1
        elif user_input in userLetters:
                print("Nope, you used the letter already :( ")
     
    print()
    if life == 0:
        print("You Lost. The word was %s." % pick)
    else:
        print("You Won! The word was %s." % pick)

def printWord(pick, userLetters):
    print()
    for x in pick:
        if x in userLetters:
            print(x + " ", end = " ")
        else:
            print("_ ", end = " ")
    print()
  

hangman()

