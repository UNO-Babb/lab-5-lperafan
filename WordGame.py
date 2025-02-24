#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    result = ""
    for i in range(len(myGuess)):
        if inSpot(myGuess[i], word, i):
            result += myGuess[i].upper()
        elif inWord(myGuess[i], word):
            result += myGuess[i].lower()
        else:
            result += "*"
    return result


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList).strip()
    #print("Word to guess (for testing):", todayWord)

    #User should get 6 guesses to guess
    attempts = 6
    for i in range(attempts):
        myGuess = input("Enter your guess: ").strip()
        if len(myGuess) != len(todayWord):
            print(f"Please enter a {len(todayWord)}- letter word.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The word was: {todayWord}")
    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
