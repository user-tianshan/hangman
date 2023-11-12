# Hangman
## Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

## This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

### Initialisation function
   The initialisation function has the following attributes:
  - word_list,  the list of words
  - word_guessed, the word from the list to be guessed by the player
  - num_lives,  the number of lives remaining following a wrong guess for a letter
  - list_of_guesses, a list of correct and incorrect guesses
  - word_length,  this a boolean to initially make blanks for the word and to determine the number of unique letters
  - game_not_over,  boolean set to false when the game has ended


### check_guess function
  The check_guess function checks if the guessed letter is in the word. It sets and returns the game_not_over boolean as false if the num_letters or num_lives reduce to zero which ends the game. It also initially sets the blank word with the correct number of letters and determines the number of unique letters in the word 

### ask_for_input function
  The ask_for_input function inputs and checks that the guessed letter is a single alphabetical letter and adds it to the list_of_guesses and disallows repeat guesses.

