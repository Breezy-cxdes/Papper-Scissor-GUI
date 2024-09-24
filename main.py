import random
import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Function to decide winner
def decide_winner(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Display computer's choice
    label_computer.config(text=f"Computer chose: {computer_choice}")

    # Determine winner based on game rules
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Display the result
    label_result.config(text=result)

# Function to handle user input for Rock
def rock():
    decide_winner("Rock")

# Function to handle user input for Paper
def paper():
    decide_winner("Paper")

# Function to handle user input for Scissors
def scissors():
    decide_winner("Scissors")

# Create GUI elements
label_title = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 16))
label_title.pack(pady=20)

button_rock = tk.Button(window, text="Rock", width=15, height=2, command=rock)
button_rock.pack(pady=10)

button_paper = tk.Button(window, text="Paper", width=15, height=2, command=paper)
button_paper.pack(pady=10)

button_scissors = tk.Button(window, text="Scissors", width=15, height=2, command=scissors)
button_scissors.pack(pady=10)

label_computer = tk.Label(window, text="Computer chose: ", font=("Arial", 12))
label_computer.pack(pady=20)

label_result = tk.Label(window, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
