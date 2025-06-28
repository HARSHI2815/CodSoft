import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    # Grab the length input by the user
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length has to be more than zero.")
    except ValueError:
        # Show a pop-up if the input is not a positive number
        messagebox.showerror("Oops!", "Please enter a valid positive number for password length.")
        return

    # Characters we’ll use: letters (upper + lower), digits, and symbols
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Pick random characters to build the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    # Show the generated password on the screen
    password_var.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add a label and entry box for the user to type desired length
tk.Label(root, text="How long should the password be?").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Button that triggers password generation
generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

# Label where the password will appear
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 14), fg="green")
password_label.pack(pady=10)

# Start the GUI loop
root.mainloop()


