
conditions_not_met = True

while (conditions_not_met) :
    guess = input("Enter a single letter :")
    if (len(guess) == 1 and (guess.isalpha())):
        message = guess, "Good guess"
        conditions_not_met = False
    else:
        message = guess, "Invalid letter. Please, enter a single alphabetical character."
    print(message)