import random
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
import hangman_words

chosen_word=random.choice(hangman_words.word_list)
print(f'Pssst, the solution is {chosen_word}.')
display=[]
letter_length=len(chosen_word)
lives=6
for x in range(letter_length):
    display += "_"
print(display)
end_of_game= False
while not end_of_game:
    guess=input("Guess a letter: ").lower()
    for position in range(letter_length):
        letter= chosen_word[position]
        if letter== guess:
          display[position]=letter
    if guess not in chosen_word:
      lives -=1
      if  lives ==0:
        end_of_game= True
        print("You lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("You have won")
    print(stages[lives])