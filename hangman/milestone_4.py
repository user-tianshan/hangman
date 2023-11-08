import random

word_list = ["Apple", "Orange", "Pear", "Grape", "Peach"]
print(word_list)

word = random.choice(word_list)
print(word)

conditions_not_met = True
guess_not_in_word = True
message = ""

while (conditions_not_met or guess_not_in_word) :
    guess = input("Enter a single letter :")
    if (len(guess) == 1 and (guess.isalpha())):
        conditions_not_met = False
        if word.count(guess):
            print("Good guess!", guess, "is in the word.")
            guess_not_in_word = False
            break
        else:
            print( "Sorry,", guess, " is not in the word. Try again.")
            continue
    else:
        message = guess, "Invalid letter. Please, enter a single alphabetical character."
    print(message)

