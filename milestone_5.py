import random #A random word from the list
class Hangman: #the properties of the list that inlcudes all the words that can be used
    def __init__(self, word_list, num_lives=5): #executes the function and the numbers of the lives for the user 
        self.word_list = word_list
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = [] #initialising Hangman

    def check_guess(self, guess): #checking users guess
        guess = guess.lower() #user inputs lower case answer 
        if guess in self.word: #is the users guess in the random choice word 
            print(f'Good guess! {guess} is in the word.') #positive response to users guess, if guessed correctly 
            letter_found = False #flag to track if a new letter is found 
            for i, letter in enumerate(self.word): #number of iterations from the random choice word 
                if letter == guess: 
                    self.word_guessed[i] = guess
                    self.num_letters -= 1 #number of lives reduced if incorrect 
                if self.wordguessed[i] == '':  #to check if this letter has not been revealed before
                    letter_found = True
                    self.word_guessed[i] = guess
        if letter_found:
            self.num_letters -= 1.
        else:
            self.num_lives -= 1 
            print(f"Sorry, {guess} is not in the word.") #if user guesses incorrectly, negative response 
            print(f"You have {self.num_lives} lives left.") #how many user lives left to guess, after incorrect answer 
    def ask_for_input(self):
     guess = '' #initialised guess variable
    while True:
        guess = input('Enter a single letter: ') #user inputs guess
        if len(guess) == 1 and guess.isalpha(): #checks if guess is a single alphabetical letter
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character") #asking user for valid input if incorrect 
    check_guess(guess) 
    def ask_for_input(self):
        guess = ''
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) == 1 and guess.isalpha():
                if guess in self.list_of_guesses:  # Step 1:to check if guess is already in the list_of_guesses
                    print("You already tried that letter!")
                else:  # if guess is a single alphabetical character and not in list_of_guesses
                    self.check_guess(guess)  # call check_guess method
                    self.list_of_guesses.append(guess)  #append the guess to list_of_guesses
                    break
            else:
                print("Invalid letter. Please, enter a single alphabetical character")
    Hangman_game=[]
    Hangman_game.ask_for_input()
    def play_game(word_list): #function that plays the hangman game
     num_lives = 5 #number of lives for user 
     game = Hangman(word_list, num_lives) #this function initialises the hangman game with the given word list and a set number of lives
     while True:
        if game.num_lives == 0:
            print('You lost!') #message when user loses 
            break
        elif game.num_letters > 0: #the user is prompted until the game is won or lost 
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!') #message when user wins 
            break #current game ends