import random
words_list= ['strawberry', 'kiwi', 'pear', 'oranges', 'grapes']
word = random.choice(words_list)
print('Randomly chosen word:', word)
guess= input ('Enter a single letter: ')
print('You entered:', guess)
guess= input ('Enter a single letter: ')
if len(guess) == 1 and guess.alphabet():
    print('Good guess!')
else:
    print('Oops! that is not a valid input') 