import tkinter as tk
from random import randint

# Function to generate a random number
def generate_random_number():
    global random_number, attempts
    random_number = randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    result_label.config(text="Guess the number between 1 and 100")

# Function to check the user's guess
def check_guess():
    global attempts
    try:
        guess = int(guess_entry.get())
        attempts += 1
        
        if guess < random_number:
            feedback = "Too low! Try again."
        elif guess > random_number:
            feedback = "Too high! Try again."
        else:
            feedback = f"Correct! It took you {attempts} attempts."
            reset_game()
        
        result_label.config(text=feedback)
        attempts_label.config(text=f"Attempts: {attempts}")
    
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Function to reset the game
def reset_game():
    guess_entry.delete(0, tk.END)
    generate_random_number()

# GUI setup
root = tk.Tk()
root.title("Guessing Game")

# Instruction Label
instruction_label = tk.Label(root, text="Enter your guess:")
instruction_label.grid(row=0, column=0, padx=10, pady=10)

# Guess Entry
guess_entry = tk.Entry(root)
guess_entry.grid(row=0, column=1, padx=10, pady=10)

# Check Guess Button
check_button = tk.Button(root, text="Check Guess", command=check_guess)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Guess the number between 1 and 100")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Attempts Label
attempts_label = tk.Label(root, text="Attempts: 0")
attempts_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Initialize Game
generate_random_number()

# Run the application
root.mainloop()
