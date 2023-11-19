import random
words_list = ['strawberry', 'kiwi', 'pear', 'oranges', 'grapes']
#list of words
word = random.choice(words_list)
#randomly chooses the word from the list
def check_guess(guess):
#convert the guess to lower case
    guess = guess.lower()
#check if guess is in the word
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
def ask_for_input():
    guess = '' #initialised guess variable
    while True:
        guess = input('Enter a single letter: ') #user inputs guess
        if len(guess) == 1 and guess.isalpha(): #checks if guess is a single alphabetical letter
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") #asking user for valid input if incorrect 
    check_guess(guess) 
ask_for_input() #calls function after breaking out of the loop 