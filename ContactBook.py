import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"


class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Contact Book")

        self.contacts = []  # will hold Contact instances

        self.create_widgets()
        self.selected_contact_index = None  # keep track of selected contact in list

    def create_widgets(self):
        # Labels and entries
        tk.Label(self.root, text="Contact Name").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

        tk.Label(self.root, text="Phone Number").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=5)

        tk.Label(self.root, text="Email").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=2, column=1, sticky='ew', padx=5, pady=5)

        tk.Label(self.root, text="Address").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.address_entry = tk.Entry(self.root)
        self.address_entry.grid(row=3, column=1, sticky='ew', padx=5, pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Add Contact", command=self.add_contact).grid(row=0, column=0, padx=3)
        tk.Button(btn_frame, text="Update Selected", command=self.update_contact).grid(row=0, column=1, padx=3)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_contact).grid(row=0, column=2, padx=3)
        tk.Button(btn_frame, text="Search", command=self.search_contacts).grid(row=0, column=3, padx=3)
        tk.Button(btn_frame, text="Show All", command=self.display_contacts).grid(row=0, column=4, padx=3)

        # Treeview for showing contacts
        self.tree = ttk.Treeview(self.root, columns=("Name", "Phone", "Email", "Address"), show='headings')
        self.tree.heading("Name", text="Contact Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")

        self.tree.column("Name", width=140)
        self.tree.column("Phone", width=100)
        self.tree.column("Email", width=180)
        self.tree.column("Address", width=200)

        self.tree.grid(row=5, column=0, columnspan=2, sticky='nsew', padx=5)

        # Bind selecting an item in the treeview
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        # Make columns and rows expandable
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(5, weight=1)

    def add_contact(self):
        # Get info from entries
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        # Basic validation
        if not name or not phone:
            messagebox.showwarning("Oops!", "Contact name and phone are must-have fields.")
            return

        # Check for duplicate phone number
        if any(c.phone == phone for c in self.contacts):
            messagebox.showerror("Error", "Phone number already exists in contacts.")
            return

        # Add new contact
        self.contacts.append(Contact(name, phone, email, address))
        messagebox.showinfo("Nice!", "Contact added.")
        self.clear_entries()
        self.display_contacts()

    def display_contacts(self):
        # Clear current list
        for item in self.tree.get_children():
            self.tree.delete(item)

        for contact in self.contacts:
            self.tree.insert('', 'end', values=(contact.name, contact.phone, contact.email, contact.address))

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            self.selected_contact_index = None
            return

        index = self.tree.index(selected[0])
        self.selected_contact_index = index

        contact = self.contacts[index]

        # Fill the entries with the contact info
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact.name)

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact.phone)

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact.email)

        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, contact.address)

    def update_contact(self):
        if self.selected_contact_index is None:
            messagebox.showwarning("Hold on!", "Please select a contact to update.")
            return

        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Oops!", "Store name and phone can't be empty.")
            return

        # Check if new phone duplicates others (except itself)
        for idx, c in enumerate(self.contacts):
            if idx != self.selected_contact_index and c.phone == phone:
                messagebox.showerror("Error", "Another contact with this phone already exists.")
                return

        # Update the contact
        contact = self.contacts[self.selected_contact_index]
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address

        messagebox.showinfo("Success", "Contact updated.")
        self.display_contacts()
        self.clear_entries()
        self.selected_contact_index = None

    def delete_contact(self):
        if self.selected_contact_index is None:
            messagebox.showwarning("Hey!", "Select a contact first to delete.")
            return

        contact = self.contacts[self.selected_contact_index]
        confirm = messagebox.askyesno("Confirm", f"Delete contact '{contact.name}'?")
        if confirm:
            self.contacts.pop(self.selected_contact_index)
            messagebox.showinfo("Deleted", "Contact removed.")
            self.display_contacts()
            self.clear_entries()
            self.selected_contact_index = None

    def search_contacts(self):
        search_term = simpledialog.askstring("Search", "Search by store name or phone:")
        if not search_term:
            return

        search_term = search_term.lower()
        results = [c for c in self.contacts if search_term in c.name.lower() or search_term in c.phone]

        # Show results in treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        for c in results:
            self.tree.insert('', 'end', values=(c.name, c.phone, c.email, c.address))

        if not results:
            messagebox.showinfo("No luck!", "No contacts matched your search.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x400")
    app = ContactBookApp(root)
    root.mainloop()