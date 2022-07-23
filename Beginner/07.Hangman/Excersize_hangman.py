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

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_" for i in chosen_word]
end_of_game = False 
lives = 6 

while not end_of_game:
    guess = input("Guess a letter : ").lower() 

    for i in range(len(chosen_word)): 
        if guess in chosen_word[i]:
            display[i] = guess 

    # 만약 guess 가 display에 없다면 틀린것이므로 목숨을 차감한다.
    if guess not in display:
        lives -= 1 
        if lives == 0 : 
            end_of_game = True 
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("The game is End, You Win")

    print("lives :", lives)
    print(stages[lives])
