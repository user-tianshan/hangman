class Hangman:
    import random

    def __init__(self, word_list = [], num_lives = 5):

        self.word = word_list
        self.word_guessed = []
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
           

    def check_guess(self, guess, word):
        self.guess = guess.lower()
        self.word =  word.lower()
                    
        if self.num_lives == 5 : 
            for n in range(0, (len(self.word))):
                self.word_guessed.insert(n, "_")
            self.num_letters = len(set(self.word)) + 1       
            self.num_lives -= 1
      
        for n in range(0, len(self.word)):
            if (self.guess == self.word[n]):
                print("Good guess!", self.guess, "is in the word.")
                self.word_guessed[n] = guess
                self.num_letters -= 1
                print(self.word_guessed)
                print(self.num_letters, "letters remaining")
                continue

            elif word.count(guess) == 0:
                print("Sorry,", guess, "is not in the word")
                self.num_lives -= 1
                print("You have", self.num_lives, "lives left")
                break
      
            
                
    def ask_for_input(self):
        self.word_list = ["Apple", "Oraange", "Peear", "Graepe", "Peaach"]
        print(self.word_list)
        self.word = self.random.choice(self.word_list)
        print(self.word)
        conditions_not_met = True
        while (conditions_not_met):
            guess = input("Enter a single letter :")
            if ((len(guess) == 1 and (guess.isalpha())) == False):
                print(guess, "Invalid letter. Please, enter a single alphabetical character.")
            
            elif self.list_of_guesses.count(guess):
                   print("You already tried that letter")
            else:
                self.check_guess(guess, self.word)
                self.list_of_guesses.append(guess)
          
my_hangman = Hangman()
my_hangman.ask_for_input()


    

