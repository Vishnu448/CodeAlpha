import random

def choose_word():
    # List of words to choose from
    words = ['python', 'development', 'hangman', 'challenge', 'programming']
    return random.choice(words)

def display_current_state(word, guessed_letters):
    # Display the current state of the word with underscores for unguessed letters
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman_game():
    word = choose_word()  # Choose a random word
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display current state of the word
        print(f"\nCurrent state: {display_current_state(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Get user's guess
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")
    
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    hangman_game()
