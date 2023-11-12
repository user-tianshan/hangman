class Hangman:
    import random

    game_not_over = True
    num_letters = 0

    def __init__(self, word_list = [], num_lives = 0, word_length = True, game_not_over = True):

        self.word = word_list
        self.word_guessed = []
       # self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.word_length = word_length
        self.game_not_over = game_not_over
       

    def check_guess(self, guess, word, num_lives):
        """This function checks if the guessed letter is in the word """
        self.guess = guess.lower()
        self.word =  word.lower()
        self.num_lives = num_lives
                          
        if self.word_length == True : 
            for n in range(0, (len(self.word))):
                self.word_guessed.insert(n, "_")
            self.num_letters = len(set(self.word)) + 1      
            self.word_length =  False
      
        for n in range(0, len(self.word)):
            if (self.guess == self.word[n]):
                print("Good guess!", self.guess, "is in the word.")
                self.word_guessed[n] = guess
                self.num_letters -= 1
                print(self.word_guessed)
                print(self.num_letters, "letters remaining")
                if(self.num_letters == 0):
                   self.game_not_over = False
                   print("Congratulations. You won the game!")
                   return self.game_not_over
                continue

            else:
                if  self.word.count(self.guess) == 0:
                    print("Sorry,", guess, "is not in the word")
                    self.num_lives -= 1
                    print("You have", self.num_lives, "lives left")
                    if(self.num_lives == 0):
                        self.game_not_over = False
                        print("You lost!")
                        return self.game_not_over
                    break
      
            
                
    def ask_for_input(self):
        """ Receives input from the user and checks for the correct format before passing to the check_guess function"""
        print(self.word_list)
        self.word = self.random.choice(self.word_list)
        print(self.word)
        while (self.game_not_over):
            guess = input("Enter a single letter :")
            if ((len(guess) == 1 and (guess.isalpha())) == False):
                print(guess, "Invalid letter. Please, enter a single alphabetical character.")
            
            elif self.list_of_guesses.count(guess):
                print("You already tried that letter")
          
            else:
                self.check_guess(guess, self.word, self.num_lives)
                self.list_of_guesses.append(guess)
        return self.game_not_over
             
          

    def play_game(self, word_list):
        """This function starts the game"""
        num_lives = 5
        self.word_list = word_list
        game = Hangman(word_list, num_lives)
        game.ask_for_input()
           

my_hangman = Hangman()
my_hangman.play_game( ["Apple", "Oraange", "Peear", "Graepe", "Peaach"])







 


    