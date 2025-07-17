import random

# Hangman drawings (from 0 mistakes to full hang)
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

print("Hi there! Welcome to my hangman game, where you have to guess a random word! but if you don't, a man will DIE. Have Fun!")

categories = {
    "Animals": ["lion", "elephent", "monkey"],
    "Names": ["john", "kevin", "steve"],
    "Fruit": ["tomatoe", "apple", "orange"]
}

chosen_cat = input("Choose a category: Animals, Names or Fruit: ").lower().capitalize()

if chosen_cat not in categories:
    print("Go back to 3rd grade and learn how to read")
    exit()
else:
    chosen_word = random.choice(categories[chosen_cat])

print("\nAlright! A word has been chosen. You shall BEGIN.")


word_display = ['_' for _ in chosen_word]
guessed_letters = []
attempts_left = 6

print(f"\nCategory: {chosen_cat}")
print("Welcome to Hangman!\n")

# Keep a counter for wrong attempts (to show ASCII art)

while attempts_left > 0 and '_' in word_display:
    # Show hangman image
    print(HANGMAN_PICS[6 - attempts_left])

    print("\nWord:", ' '.join(word_display))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[idx] = guess
        print("✅ Correct!")
    else:
        attempts_left -= 1
        print("❌ Wrong!")

# Final state
print(HANGMAN_PICS[6 - attempts_left])

if '_' not in word_display:
    print(f"\n🎉 You won! The word was: {chosen_word.capitalize()}")
else:
    print(f"\n💀 Game over! The word was: {chosen_word.capitalize()}")
