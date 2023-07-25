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

import random
end_of_game=False 
word_list = ["aardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
letter_length= len(chosen_word)
lives = 6
print(f'Pssst, the solution is {chosen_word}.')
display=[]
for _ in range(letter_length):
    display += "_"
  
while not end_of_game:
    guess= input("Guess a letter: ").lower()
    for position in range(letter_length):
        letter=chosen_word[position]
        if letter== guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True   
            print("You have Lost") 
    print(f"{' '.join(display)}")
    print(display)
    if "_" not in display:
        end_of_game= True
        print("You Win!") 
    print(stages[lives])                
    