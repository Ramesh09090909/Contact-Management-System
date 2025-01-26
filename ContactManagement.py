import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# List to store contacts
contacts = []

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts.append({"Name": name, "Phone": phone, "Email": email})
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields are required!")

# Function to update the contact list display
def update_contact_list():
    contact_list_text.config(state=tk.NORMAL)  # Enable Text widget for modification
    contact_list_text.delete(1.0, tk.END)  # Clear current contact list
    for idx, contact in enumerate(contacts):
        contact_list_text.insert(tk.END, f"{idx + 1}. Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}\n")
    contact_list_text.config(state=tk.DISABLED)  # Disable Text widget after modification

# Function to edit a contact
def edit_contact():
    try:
        contact_idx = int(simpledialog.askstring("Edit Contact", "Enter the index number to edit:")) - 1
        if 0 <= contact_idx < len(contacts):
            contact = contacts[contact_idx]
            name = simpledialog.askstring("Edit Name", f"Edit Name (current: {contact['Name']}):")
            phone = simpledialog.askstring("Edit Phone", f"Edit Phone (current: {contact['Phone']}):")
            email = simpledialog.askstring("Edit Email", f"Edit Email (current: {contact['Email']}):")
            if name and phone and email:
                contact['Name'] = name
                contact['Phone'] = phone
                contact['Email'] = email
                update_contact_list()
            else:
                messagebox.showerror("Error", "All fields must be filled to update the contact!")
        else:
            messagebox.showerror("Error", "Invalid contact number! Please enter a valid contact number from the list.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid contact number!")

# Function to delete a contact
def delete_contact():
    try:
        contact_idx = int(simpledialog.askstring("Delete Contact", "Enter the index number to delete:")) - 1
        if 0 <= contact_idx < len(contacts):
            del contacts[contact_idx]
            update_contact_list()
        else:
            messagebox.showerror("Error", "Invalid contact number! Please enter a valid contact number from the list.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid contact number!")

# Function to save contacts to a file
def save_contacts():
    try:
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)
        messagebox.showinfo("Info", "Contacts saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving: {e}")

# Function to load contacts from a file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            global contacts  # Use global contacts to update it with loaded data
            contacts = json.load(file)
        update_contact_list()
    except FileNotFoundError:
        messagebox.showinfo("Info", "No saved contacts found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading contacts: {e}")

# Create the main window
window = tk.Tk()
window.title("Contact Management System")

# Label and Entry widgets for contact details
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

phone_label = tk.Label(window, text="Phone:")
phone_label.grid(row=1, column=0, padx=10, pady=5)

phone_entry = tk.Entry(window)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

email_label = tk.Label(window, text="Email:")
email_label.grid(row=2, column=0, padx=10, pady=5)

email_entry = tk.Entry(window)
email_entry.grid(row=2, column=1, padx=10, pady=5)

# Buttons for actions
add_button = tk.Button(window, text="Add Contact", command=add_contact)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

edit_button = tk.Button(window, text="Edit Contact", command=edit_contact)
edit_button.grid(row=4, column=0, pady=10)

delete_button = tk.Button(window, text="Delete Contact", command=delete_contact)
delete_button.grid(row=4, column=1, pady=10)

save_button = tk.Button(window, text="Save Contacts", command=save_contacts)
save_button.grid(row=5, column=0, pady=10)

load_button = tk.Button(window, text="Load Contacts", command=load_contacts)
load_button.grid(row=5, column=1, pady=10)

# Display current contact list
contact_list_label = tk.Label(window, text="Contact List:")
contact_list_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

contact_list_text = tk.Text(window, width=40, height=10, wrap=tk.WORD, state=tk.DISABLED)
contact_list_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Run the main event loop
window.mainloop()
