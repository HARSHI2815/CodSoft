pip install tk
import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, window):
        self.window = window
        self.window.title("My To-Do List")

        # This will hold our tasks as dictionaries with name and completion status
        self.tasks = []

        # Listbox: Where we'll show the tasks
        self.task_list = tk.Listbox(self.window, height=12, width=50)
        self.task_list.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # Entry box: User types a new task here
        self.new_task_entry = tk.Entry(self.window, width=40)
        self.new_task_entry.grid(row=1, column=0, padx=20)

        # Button to add the new task
        self.add_task_button = tk.Button(
            self.window, text="Add Task", width=15, command=self.add_task)
        self.add_task_button.grid(row=1, column=1)

        # Button to remove the selected task
        self.remove_task_button = tk.Button(
            self.window, text="Remove Task", width=15, command=self.remove_task)
        self.remove_task_button.grid(row=2, column=0, pady=10)

        # Button to mark the selected task as done
        self.mark_done_button = tk.Button(
            self.window, text="Mark as Done", width=15, command=self.mark_task_done)
        self.mark_done_button.grid(row=2, column=1, pady=10)

    def add_task(self):
        task_text = self.new_task_entry.get().strip()  # Remove extra spaces
        if task_text == "":
            messagebox.showwarning("Oops!", "You need to write something before adding!")
            return

        # Add the task to our list with 'done' status False by default
        self.tasks.append({"task": task_text, "done": False})
        self.new_task_entry.delete(0, tk.END)  # Clear the input box
        self.refresh_task_list()

    def remove_task(self):
        try:
            selected_index = self.task_list.curselection()[0]
        except IndexError:
            messagebox.showwarning("Oops!", "Please select a task to remove.")
            return

        task_to_remove = self.tasks.pop(selected_index)
        self.refresh_task_list()
        messagebox.showinfo("Removed!", f"Removed: '{task_to_remove['task']}'")

    def mark_task_done(self):
        try:
            selected_index = self.task_list.curselection()[0]
        except IndexError:
            messagebox.showwarning("Oops!", "Select a task to mark as done.")
            return

        # Mark the task as done
        self.tasks[selected_index]["done"] = True
        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_list.delete(0, tk.END)  # Clear everything first

        for task in self.tasks:
            status = "✓ Done" if task["done"] else "❗ Pending"
            display_text = f"{task['task']} — {status}"
            self.task_list.insert(tk.END, display_text)


def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()