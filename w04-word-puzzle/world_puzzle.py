"""
Author: ASILATSA DOUNYA BRANDON
Projects: world_puzzle

"""
# store the secret in the program, lower case and length
secret_word = "mosiah"
secret_word = secret_word.lower()
secret_word_count = len(secret_word)

user_guess = ""
number_guesses = 0

print("Welcome to the word guessing game!\n")

for _ in secret_word:
    print("_", end="")

print()    

# prompt the user for a guess and looping as long as the guess is not correct
while user_guess != secret_word:
    user_guess = input("\nWhat is your guess? ").lower()
    # calculate the number of guesses
    number_guesses += 1

    # verify that the length of the guess and the secret word are equal
    if len(user_guess) != secret_word_count:
        print("Sorry, the guess must have the same number of letters as the secret word.")
    
    # Initiation of the hint to the user
    if user_guess != secret_word:
        print("Your hint is: ", end="")

        for index in range(secret_word_count):
            guessed_letter = user_guess[index]
            secret_letter = secret_word[index]
  
            if guessed_letter == secret_letter:
                print((guessed_letter.upper()), end="")
            elif guessed_letter in secret_word:
                print((guessed_letter.lower()), end="")
            else:
                print("_", end="")      
    
print("\nCongratulations! You guessed it")
# display the number of guesses
print(f"\nIt took you {number_guesses} guesses.")


