import tkinter as tk
import random

OPTIONS = ['Rock', 'Paper', 'Scissors']
user_score = 0
computer_score = 0

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(OPTIONS)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Paper' and computer_choice == 'Rock') or
        (user_choice == 'Scissors' and computer_choice == 'Paper')
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    
    result_label.config(text=result)
    score_label.config(text=f"You: {user_score}  Computer: {computer_score}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create labels
result_label = tk.Label(window, text="Make your choice:")
result_label.pack()

score_label = tk.Label(window, text="You: 0  Computer: 0")
score_label.pack()

# Create buttons
for option in OPTIONS:
    button = tk.Button(window, text=option, command=lambda o=option: play_game(o))
    button.pack()

# Create a quit button
quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack()

# Start the GUI event loop
window.mainloop()
