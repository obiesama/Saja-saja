import tkinter as tk
from tkinter import messagebox

# List of romantic questions
questions = [
    "What is your partner's favorite color?",
    "Where was your first date?",
    "What is your partner's favorite food?",
    "What song reminds you of your love?",
    "What is one thing you love most about your partner?"
]

answers = []
current_question = 0
score = 0

# Function to display next question
def next_question():
    global current_question, score

    # Get the user's answer and move to the next question
    user_answer = entry.get()
    if user_answer.strip():  # If the answer is not empty
        answers.append(user_answer)
        score += 10  # Give points for answering
    entry.delete(0, tk.END)  # Clear the input field

    current_question += 1

    if current_question < len(questions):
        question_label.config(text=questions[current_question])
    else:
        show_result()

# Function to show love score and romantic message
def show_result():
    global score
    window.destroy()  # Close the game window

    max_score = len(questions) * 10
    if score >= max_score * 0.8:
        message = "Wow! You two are a perfect match! 💑💖"
    elif score >= max_score * 0.5:
        message = "Great job! Your love is strong and growing! 💞"
    else:
        message = "You have room to learn more about each other! Keep the love alive! ❤️"

    # Show the result in a message box
    messagebox.showinfo("Love Score", f"Your Love Score: {score}/{max_score}\n{message}")

# Create the main game window
window = tk.Tk()
window.title("Romantic Couple Game 💖")
window.geometry("500x300")
window.config(bg="#ffcccb")

# Question Label
question_label = tk.Label(window, text=questions[0], font=("Arial", 14), bg="#ffcccb", wraplength=400)
question_label.pack(pady=20)

# Input Field
entry = tk.Entry(window, font=("Arial", 12), width=40)
entry.pack(pady=10)

# Next Button
next_button = tk.Button(window, text="Next 💕", font=("Arial", 12), bg="pink", command=next_question)
next_button.pack(pady=10)

# Run the GUI
window.mainloop()
