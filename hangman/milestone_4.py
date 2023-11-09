class Hangman:
    import random

    def __init__(self, word_list, num_lives = 5):

        self.word = word_list
        self.word_guessed = []
        self.num_letters = 0
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    

