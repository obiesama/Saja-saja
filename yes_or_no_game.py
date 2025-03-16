import tkinter as tk
import random
from tkinter import messagebox

# List of romantic questions
questions = [
    "Do you love me? 💖",
    "Will you always be with me? 💑",
    "Am I the love of your life? 😍",
    "Will you take me on a date? 🍽️💕",
    "Can I have a hug? 🤗"
]

current_question = 0

# Function to move the "No" button randomly
def move_no_button(event=None):
    new_x = random.randint(50, 400)
    new_y = random.randint(50, 300)
    no_button.place(x=new_x, y=new_y)

# Function to show next question or end the game
def next_question():
    global current_question
    current_question += 1

    if current_question < len(questions):
        question_label.config(text=questions[current_question])
    else:
        messagebox.showinfo("Game Over", "You picked 'Yes' every time! You are the best partner ever! 💕😍")
        window.quit()  # Close the game

# Create the main game window
window = tk.Tk()
window.title("💖 Romantic Yes or No Game 💖")
window.geometry("500x400")
window.config(bg="#ffcccb")

# Question Label
question_label = tk.Label(window, text=questions[0], font=("Arial", 16, "bold"), bg="#ffcccb")
question_label.pack(pady=50)

# "Yes" Button - When clicked, show next question
yes_button = tk.Button(window, text="Yes 💕", font=("Arial", 14, "bold"), bg="lightgreen", command=next_question)
yes_button.place(x=150, y=200)

# "No" Button - Moves when hovered or clicked
no_button = tk.Button(window, text="No 😢", font=("Arial", 14, "bold"), bg="red")
no_button.place(x=280, y=200)
no_button.bind("<Enter>", move_no_button)  # Move when hovered
no_button.bind("<Button-1>", move_no_button)  # Move when clicked

# Run the game
window.mainloop()
