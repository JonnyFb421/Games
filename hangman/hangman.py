import random

def get_hangman_words():
    return [
        'Clover Rover October'
    ]

def display_hangman(incorrect_guesses):
    if incorrect_guesses == 0:
        print("""
___________  
|         |  
|            
|            
|            
|            
|            
""")
    elif incorrect_guesses == 1:
        print("""
___________  
|         |  
|         0  
|            
|            
|            
|            
""")
    elif incorrect_guesses == 2:
        print("""
___________  
|         |  
|         0  
|         |  
|            
|            
|            
""")
    elif incorrect_guesses == 3:
        print("""
___________  
|         |  
|         0  
|        /|  
|            
|            
|            
""")
    elif incorrect_guesses == 4:
        print("""
___________  
|         |  
|         0  
|        /|\ 
|            
|            
|            
""")
    elif incorrect_guesses == 5:
        print("""
___________  
|         |  
|         0  
|        /|\ 
|        /   
|            
|            
""")
    elif incorrect_guesses == 6:
        print("""
___________  
|         |  
|         0  
|        /|\ 
|        / \ 
|            
|            
""")


def display_word_progress(guessed_letters, word):
    word_progress = []
    for letter in word:
        if letter.lower() in guessed_letters or letter == ' ':
            word_progress.append(letter)
        else:
            word_progress.append('_')
    print(' '.join(word_progress))


def get_guess_from_user(guessed_letters):
    guess = input(f"Letters you have guessed {guessed_letters}.\nGuess a new letter: ")
    guess = guess.lower().strip()
    if guess in guessed_letters or len(guess) > 1:
        return None
    else:
        return guess


def is_puzzle_solved(guessed_letters, word):
    puzzle_is_solved = True
    for letter in word.lower().replace(' ', '').strip():
        if letter not in guessed_letters:
            puzzle_is_solved = False
    return puzzle_is_solved


def is_man_hanged(incorrect_guesses, max_incorrect_guesses):
    return incorrect_guesses >= max_incorrect_guesses


def is_guess_correct(guess, word):
    return guess in word.lower()


def create_new_game():
    incorrect_guesses = 0
    max_guesses = 6
    guessed_letters = []
    game_is_over = False
    word = random.choice(get_hangman_words())

    # Game loop
    while not game_is_over:
        # Get valid guess from user
        guess = None
        while guess is None:
            guess = get_guess_from_user(guessed_letters)
        # Add guess to guessed_letters list
        guessed_letters.append(guess)
        # Increment incorrect guesses if the guess was incorrect
        if not is_guess_correct(guess, word):
            incorrect_guesses += 1
        display_hangman(incorrect_guesses)
        display_word_progress(guessed_letters, word)
        # Check to see if the puzzle is solved
        if is_puzzle_solved(guessed_letters, word):
            print("You win!")
            return True
        if is_man_hanged(incorrect_guesses, max_guesses):
            print("You lose!")
            return False

def start_hangman_gameloop():
    wins = 0
    losses = 0
    play_again = True
    while play_again:
        game_result = create_new_game()
        if game_result is True:
            wins += 1
        else:
            losses += 1
        print(f"Wins: {wins}\nLosses: {losses}")
        play_again_input = input("Would you like to play again? Y/N")
        if play_again_input.lower().startswith('y'):
            play_again = True
        else:
            play_again = False


if __name__ == '__main__':
    start_hangman_gameloop()
