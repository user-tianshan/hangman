import random

word_list = ["Apple", "Orange", "Pear", "Grape", "Peach"]
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Enter a single letter :")

if (len(guess) ==1 and (guess >= 'a' and guess <= 'z') or (guess >= 'A' and guess <= 'Z')):
    print(guess, "Good guess")
else:
    print(guess, "Oops! That is not a valid input")