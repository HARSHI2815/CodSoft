import tkinter as tk
from tkinter import messagebox
import random

# Track scores
player_score = 0
cpu_score = 0

# Options available
options = ["Rock", "Paper", "Scissors"]

# Function to decide winner
def make_choice(player_pick):
    global player_score, cpu_score

    cpu_pick = random.choice(options)

    # Show choices
    player_choice_label.config(text=f"You picked: {player_pick}")
    cpu_choice_label.config(text=f"Computer picked: {cpu_pick}")

    # Determine result
    if player_pick == cpu_pick:
        outcome = "It's a tie!"
    elif (player_pick == "Rock" and cpu_pick == "Scissors") or \
         (player_pick == "Paper" and cpu_pick == "Rock") or \
         (player_pick == "Scissors" and cpu_pick == "Paper"):
        outcome = "You win!"
        player_score += 1
    else:
        outcome = "Computer wins!"
        cpu_score += 1

    # Show result and update score
    result_label.config(text=outcome)
    score_label.config(text=f"Score | You: {player_score}  CPU: {cpu_score}")

# Reset everything
def reset():
    global player_score, cpu_score
    player_score = 0
    cpu_score = 0
    player_choice_label.config(text="You picked: ")
    cpu_choice_label.config(text="Computer picked: ")
    result_label.config(text="")
    score_label.config(text="Score | You: 0  CPU: 0")

# Exit confirmation
def quit_game():
    confirm = messagebox.askyesno("Exit Game", "Do you really want to quit?")
    if confirm:
        root.destroy()

# Setup window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("380x350")
root.resizable(False, False)

# Instruction label
tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Helvetica", 14)).pack(pady=10)

# Buttons for player input
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Rock", width=10, command=lambda: make_choice("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: make_choice("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: make_choice("Scissors")).grid(row=0, column=2, padx=5)

# Output labels
player_choice_label = tk.Label(root, text="You picked: ", font=("Helvetica", 12))
player_choice_label.pack(pady=5)

cpu_choice_label = tk.Label(root, text="Computer picked: ", font=("Helvetica", 12))
cpu_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 13, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score | You: 0  CPU: 0", font=("Helvetica", 12))
score_label.pack(pady=10)

# Bottom buttons
bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=15)

tk.Button(bottom_frame, text="Reset", width=10, command=reset).grid(row=0, column=0, padx=10)
tk.Button(bottom_frame, text="Quit", width=10, command=quit_game).grid(row=0, column=1, padx=10)

# Start the GUI loop
root.mainloop()