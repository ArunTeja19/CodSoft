import tkinter as tk
import random

# Global variables to keep track of the score
player_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

# Function to play a round
def play_round(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose {computer_choice}\n{result}")
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
    play_again_button.pack()

# Function to reset the game
def play_again():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    score_label.config(text="Player: 0  Computer: 0")
    result_label.config(text="")
    play_again_button.pack_forget()

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create labels and buttons
title_label = tk.Label(window, text="Code By ARUN TEJA", font=("Helvetica", 16))
title_label.pack(pady=10)

rock_button = tk.Button(window, text="Rock", command=lambda: play_round("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play_round("Paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_round("Scissors"))
play_again_button = tk.Button(window, text="Play Again", command=play_again)

rock_button.pack()
paper_button.pack()
scissors_button.pack()

result_label = tk.Label(window, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Player: 0  Computer: 0", font=("Helvetica", 14))
score_label.pack(pady=10)

play_again_button.pack_forget()  # Initially, the "Play Again" button is hidden


# Start the main loop
window.mainloop()
