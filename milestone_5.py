import random

class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word=random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        '''checks wether the user's guess is in the word'''
        guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
               if self.word[i] == guess:
                   self.word_guessed[i]=guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")

    def ask_for_input(self):
       '''asks for the user to guess a letter'''
       while True: 
           guess = input("Enter a single letter:")
           if not guess.isalpha():
               print("Invalid letter. Please, enter a single alphabetical character.")
           elif guess in self.list_of_guesses:
               print("You already tried that letter!")
           else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
                

def play_game(word_list):
    '''runs the code in order to run the Hangman game as expected'''
    num_lives=5
    game = Hangman(word_list,num_lives)
    while True:
      if game.num_lives == 0:
        print("You lost!")
        break
      elif game.num_letters > 0:
           game.ask_for_input()
      else:
          print("Congratulations. You won the game")
          break

if __name__ == '__main__':
    play_game(word_list = ["apple","banana","orange","pineapple","mango"])
