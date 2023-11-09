import random


def check_guess(guess, word):
    guess = guess.lower()
    if word.count(guess):
        print("Good guess!", guess, "is in the word.")
    else:
        print( "Sorry,", guess, " is not in the word. Try again.")

def ask_for_input():
    word_list = ["Apple", "Orange", "Pear", "Grape", "Peach"]
    print(word_list)
    word = random.choice(word_list)
    print(word)
    conditions_not_met = True
    while (conditions_not_met) :
        guess = input("Enter a single letter :")
        if (len(guess) == 1 and (guess.isalpha())):
            conditions_not_met = False
        else:
            message = guess, "Invalid letter. Please, enter a single alphabetical character."
            print(message)
            continue
    check_guess(guess, word)

ask_for_input()

 


    