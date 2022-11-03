"""
Hangman in the terminal, written in Python.
"""

#Random so I can chiise a random word later on
import random

#List of words to choose from, kept short and simple
words = ["food", "house", "earth", "car", "wheel", "red", "jump"]

#Asssigns random word to be used for game
gameWord = random.choice(words)

#Initializes the 'board' that will show progress, and a temporary string that will be used to compare to random word
gameBoard = []
gameBoardTempStr = ""

#Fills the board with the right amount of blanks
for i in range(len(gameWord)):
    gameBoard += "-"

#Stores the letter just guessed
letterGuess = ''

#Gives the player 2 chances to not get a letter
chances = len(gameWord) + 2

print("Welcome to Hangman, keep guessing letters until you get the word.\n")

#For quick debugging
#print(f"Game word: {gameWord}")

#Prints out board before loop for initial print
for i in range(len(gameBoard)):
        print(gameBoard[i], end=" ")

#While to keep looping until win or lose
while True:

    print(f"\nYou have {chances} chances, the word is {len(gameWord)} characters long")
    letterGuess = input("Enter your letter guess: ")

    #Replaces correct guesses in correct spot
    for i in range(len(gameWord)):
        #First if skips over already correct letters
        if gameBoard[i] == "-":
            if letterGuess == gameWord[i]:
                gameBoard[i] = letterGuess
                break

    #Outputs the game board
    for i in range(len(gameBoard)):
        print(gameBoard[i], end=" ")

    #Converts the game board list into string to be compared to chosen word 
    gameBoardTempStr = ''.join(gameBoard)

    #Handles if player wins
    if gameBoardTempStr == gameWord:
        print("\n\nYou got the whole word, Congrats you have WON!!!!!!!!")
        break

    #Reduces chances every round
    chances -= 1

    #Handles if player loses
    if chances <= 0:
        print("\n\nYou have unfortunatly ran out of chances\nGAME OVER!")
        break