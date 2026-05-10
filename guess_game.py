# =========================================
# 🎮 Python Number Guessing Game
# =========================================

# Import random module
# Used to generate random numbers
import random

# Import tkinter module
# Used to create GUI window and widgets 
import tkinter as tk

# Import messagebox
# Used for popup messages
from tkinter import messagebox


# =========================================
# CREATE MAIN WINDOW
# =========================================

# Create main application window
window = tk.Tk()

# Set title of window
window.title("Number Guessing Game")

# Set window size
window.geometry("400x500")

# Set background color
window.config(bg="lightblue")


# =========================================
# GAME VARIABLES
# =========================================

# Generate random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Total lives player has
lives = 5

# Initial score
score = 0


# =========================================
# TITLE LABEL
# =========================================

# Create game title label
title_label = tk.Label(

    # Parent window
    window,

    # Text displayed
    text="🎮 Number Guessing Game",

    # Font style
    font=("Arial", 20, "bold"),

    # Background color
    bg="lightblue",

    # Text color
    fg="darkblue"
)

# Place title on screen
title_label.pack(pady=10)


# =========================================
# GAME IMAGE 
# =========================================

# Instruction label
instruction_label = tk.Label(

    window,

    text="Guess a number between 1 and 100",

    font=("Arial", 12),

    bg="lightblue"
)

instruction_label.pack(pady=5)


# =========================================
# INPUT TEXTBOX
# =========================================

# Create textbox for user input
guess_entry = tk.Entry(

    window,

    # Font size
    font=("Arial", 16),

    # Center align text
    justify="center"
)

# Display textbox
guess_entry.pack(pady=10)


# =========================================
# RESULT LABEL
# =========================================

# Label to show result messages
result_label = tk.Label(

    window,

    text="Start Guessing...",

    font=("Arial", 14),

    bg="lightblue",

    fg="black"
)

# Display result label
result_label.pack(pady=10)


# =========================================
# LIVES LABEL
# =========================================

# Display remaining lives
lives_label = tk.Label(

    window,

    text="Lives: 5 ❤️",

    font=("Arial", 12, "bold"),

    bg="lightblue",

    fg="red"
)

# Show label
lives_label.pack()


# =========================================
# SCORE LABEL
# =========================================

# Display current score
score_label = tk.Label(

    window,

    text="Score: 0 🏆",

    font=("Arial", 12, "bold"),

    bg="lightblue",

    fg="green"
)

# Show score label
score_label.pack(pady=5)


# =========================================
# PLAY AGAIN FUNCTION
# =========================================

# Function to restart game
def play_again():

    # Access global variables
    global secret_number
    global lives

    # Ask user if they want to play again
    answer = messagebox.askyesno(

        # Popup title
        "Play Again",

        # Popup message
        "Do you want to play again?"
    )

    # If user clicks YES
    if answer:

        # Generate new random number
        secret_number = random.randint(1, 100)

        # Reset lives
        lives = 5

        # Update lives label
        lives_label.config(text="Lives: 5 ❤️")

        # Reset result label
        result_label.config(text="New Game Started!")

        # Clear input textbox
        guess_entry.delete(0, tk.END)

    # If user clicks NO
    else:

        # Close window
        window.destroy()


# =========================================
# MAIN GAME FUNCTION
# =========================================

# Function runs when button clicked
def check_guess():

    # Access global variables
    global lives
    global score
    global secret_number

    # Get value from textbox
    guess = int(guess_entry.get())

    # =====================================
    # CORRECT GUESS
    # =====================================

    # If user guessed correctly
    if guess == secret_number:

        # Increase score
        score += 10

        # Update score label
        score_label.config(
            text=f"Score: {score} 🏆"
        )

        # Show winner popup
        messagebox.showinfo(
            "Winner",
            "🎉 Correct Guess!"
        )

        # Restart game
        play_again()

    # =====================================
    # TOO HIGH
    # =====================================

    # If guess is greater
    elif guess > secret_number:

        # Reduce lives
        lives -= 1

        # Show message
        result_label.config(
            text="📈 Too High!"
        )

    # =====================================
    # TOO LOW
    # =====================================

    # If guess is smaller
    else:

        # Reduce lives
        lives -= 1

        # Show message
        result_label.config(
            text="📉 Too Low!"
        )

    # =====================================
    # UPDATE LIVES LABEL
    # =====================================

    # Update remaining lives
    lives_label.config(
        text=f"Lives: {lives} ❤️"
    )

    # =====================================
    # VERY CLOSE HINT
    # =====================================

    # Check if guess is very close
    if abs(secret_number - guess) <= 5:

        # Show hint
        result_label.config(
            text="🔥 Very Close!"
        )

    # =====================================
    # GAME OVER
    # =====================================

    # If no lives remaining
    if lives == 0:

        # Show game over popup
        messagebox.showerror(

            "Game Over",

            f"Correct number was {secret_number}"
        )

        # Restart game
        play_again()


# =========================================
# SUBMIT BUTTON
# =========================================

# Create submit button
submit_button = tk.Button(

    window,

    # Button text
    text="Submit Guess",

    # Font style
    font=("Arial", 14, "bold"),

    # Background color
    bg="green",

    # Text color
    fg="white",

    # Padding
    padx=10,
    pady=5,

    # Function to run on click
    command=check_guess
)

# Display button
submit_button.pack(pady=20)


# =========================================
# START APPLICATION
# =========================================

# Run GUI application continuously
window.mainloop()
