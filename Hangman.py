import random

def play_hangman():
    # Words aur unke hints ki list
    words_with_hints = {
        "python": "A popular programming language named after a comedy show.",
        "github": "A cloud-based service for hosting Git repositories.",
        "variable": "A container for storing data values.",
        "compiler": "Translates high-level code into machine code."
    }
    
    # Randomly ek word select karna
    word, hint = random.choice(list(words_with_hints.items()))
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()
    
    print("====== WELCOME TO HANGMAN ======")
    print(f"Hint: {hint}")
    
    # Game Loop
    while attempts > 0 and "_" in guessed_word:
        print("\nWord to guess: " + " ".join(guessed_word))
        print(f"Attempts remaining: {attempts}")
        print(f"Guessed letters: {', '.join(sorted(list(guessed_letters))) if guessed_letters else 'None'}")
        
        guess = input("Guess a letter: ").lower().strip()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        # Match check
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Wrong guess! '{guess}' is not in the word.")
            attempts -= 1
            
    # Final Result
    if "_" not in guessed_word:
        print(f"\n🎉 Congratulations! You guessed the word: {word}")
    else:
        print(f"\n💥 Game Over! You ran out of attempts. The word was: {word}")

# Game start karein
play_hangman()