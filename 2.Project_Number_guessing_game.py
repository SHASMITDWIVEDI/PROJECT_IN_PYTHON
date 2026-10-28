# PROJECT 2 – THE PERFECT GUESS
# We are going to write a program that generates a random number and 
# asks the user to guess it.
# If the player's guess is higher than the actual number, the program '
# ' "Lower number please". Similarly, if the user's guess is too low, 
# the program prints "higher number please" When the user guesses the correct number, 
# the program displays the number of guesses the player used to arrive at the number.
# Hint: Use the random module.
# Would you like me to write the Python code to complete this project, 
# or do you need help understanding how the random module works?
import random
n = random.randint(1, 100)
guesses = 0
a = -1



while (a != n):
    
    a = int(input("Enter your guess between 1 and 100: "))
    guesses += 1
    if a < n:
        print("Higher number please")
    elif a > n:
        print("Lower number please")



    


print(f"Correct! You arrived at the number in {guesses + 1} guesses.")
