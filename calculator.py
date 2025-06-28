
import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        # Get the numbers entered by the user
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = selected_operation.get()

        # Perform the selected operation
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                messagebox.showerror("Oops!", "You can't divide by zero! Try again.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Something went wrong. Please select an operation.")
            return

        # Show the result in a nice format
        label_result.config(text=f"Here’s your answer: {result}")
    except ValueError:
        messagebox.showerror("Whoops!", "Please make sure you enter valid numbers.")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Make the window a bit larger and cozy
root.geometry("400x350")

# Add a friendly welcome label
label_title = tk.Label(root, text="Hey there! Let's do some math.", font=("Arial", 16))
label_title.pack(pady=10)

# Label and entry for the first number
label_num1 = tk.Label(root, text="What's the first number?")
label_num1.pack()
entry_num1 = tk.Entry(root, width=20)
entry_num1.pack(pady=5)

# Label and entry for the second number
label_num2 = tk.Label(root, text="And what's the second number?")
label_num2.pack()
entry_num2 = tk.Entry(root, width=20)
entry_num2.pack(pady=5)

# Dropdown for selecting the operation
label_operation = tk.Label(root, text="Choose your operation:")
label_operation.pack()

selected_operation = tk.StringVar(value="Add")  # Default is 'Add'
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, selected_operation, *operations)
operation_menu.pack(pady=5)

# Button to calculate the result
button_calculate = tk.Button(root, text="Let's Calculate!", command=calculate)
button_calculate.pack(pady=10)

# Label to show the result in a fun, friendly way
label_result = tk.Label(root, text="Result will show up here!", font=("Arial", 14))
label_result.pack(pady=20)

# Start the main loop
root.mainloop()