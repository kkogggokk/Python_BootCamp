import random 
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

print(logo)
# word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = ["_" for i in chosen_word]
end_of_game = False 
lives = 6 

while not end_of_game:
    guess = input("Guess a letter : ").lower() 

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display : 
        print("이미 존재하는 chr")

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
