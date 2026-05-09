import tkinter as tk
import random
from tkinter import messagebox


window = tk.Tk()
window.title("Number Guessing Game")
window.geometry("400x400")
window.config(bg="lightblue")

# Generate random number
secret_number = random.randint(1, 100)

# Total Chances
lives = 5
score = 0

title_label = tk.Label(
    window,
    text="🎮 Number Guessing Game",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)

title_label.pack(pady=10)

guess_entry = tk.Entry(window, font=("Arial", 16))
guess_entry.pack(pady=10)

# Add Result label 
result_label = tk.Label(
    window,
    text="Enter a number between 1-100",
)

result_label.pack(pady=10)

# Add lives label 
lives_label = tk.Label(
    window,
    text="Lives:5",
    font=("Arial", 12),
    bg="lightblue"
)

lives_label.pack()

# Add Score label 
score_label = tk.Label(
    window,
    text="Score: 0",
    font=("Arial", 12),
    bg="lightblue"
)
score_label.pack()

#  Add play again function
def play_again():

    global secret_number
    global lives

    answer =  messagebox.askyesno(
        "Play Again",
        "Do you want to play again?"
    )

    if answer:

        secret_number = random.randint(1, 100)
        lives = 5

        lives_label.config(text="Lives: 5")
        result_label.config(text="New Game Started!")

        guess_entry.delete(0, tk.END)

    else:
        window.destroy()

# Create game function
# This function runs when button is clicked
def check_guess():

    global lives
    global score
    global secret_number

    guess = int(guess_entry.get())

    if guess == secret_number:

        score += 10

        score_label.config(text=f"Score: {score}")

        messagebox.showinfo("Winner", "🎉 Correct Guess!")

        play_again()

    elif guess > secret_number:

        lives -= 1

        result_label.config(text="📈 Too High!")

    else: 

        lives -= 1

        result_label.config(text="📉 Too Low!")

    lives_label.config(text=f"Lives: {lives}")

    if abs(secret_number - guess) <= 5:
        result_label.config(text="🔥 Very Close!")

    if lives == 0:

        messagebox.showerror(
            "Game Over",
            f"Correct Number was {secret_number}"
        )

        play_again()


#  Add Submit button
submit_button = tk.Button(
    window,
    text="Submit Guess",
    font=("Arial", 14),
    bg="green",
    fg="white",
    command=check_guess
)

submit_button.pack(pady=20)

window.mainloop()

