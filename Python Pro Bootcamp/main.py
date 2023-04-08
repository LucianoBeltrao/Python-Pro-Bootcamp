#Step
from hangman_art import logo
print(logo)

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
from hangman_words import word_list

number = random.randint(0, len(word_list)-1)
chosen_word = word_list[number]
print(f'Pssst, the solution is {chosen_word}.')

display=[]
for letter in chosen_word:
  display.append("_")

lives=6
  
while '_' in display:

  guess = input('Guess a letter:').lower()
  if guess in display:
    
    print(f"You've already guessed {guess}")
    print(f"{' '.join(display)}")
    print(stages[lives])
  else:
    for n in range(len(chosen_word)):
      indice = n
      if chosen_word[indice] == guess:
        display[indice] = guess
   
  
    if guess not in chosen_word:
      lives -=1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      print(stages[lives])
      
    print(f"{' '.join(display)}")
    
    if lives == 0:
      display=[]
    
if lives >0:
  print('You win.')
else:
  print('You lose.')






    


