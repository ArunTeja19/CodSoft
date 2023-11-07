import tkinter as tk
from tkinter import messagebox



def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone and email and address:
        contact_list.insert(tk.END, f"Name: {name}, Phone: {phone}, Email: {email}, Address: {address}")
        clear_entries()
    else:
        messagebox.showwarning("Warning", "All fields are required!")

def delete_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        contact_list.delete(selected_index)

def update_contact():
    selected_index = contact_list.curselection()
    if selected_index:
        selected_contact = contact_list.get(selected_index)
        contact_list.delete(selected_index)
        add_contact()
        clear_entries()
        update_button.config(state=tk.DISABLED)

def view_contacts():
    contacts = contact_list.get(0, tk.END)
    contact_details = "\n".join(contacts)
    if contact_details:
        messagebox.showinfo("Contact Details", contact_details)
    else:
        messagebox.showinfo("Contact Details", "No contacts to display.")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def on_contact_select(event):
    update_button.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Contact Book")

title_label = tk.Label(root, text="Code By ARUN TEJA", font=("Helvetica", 16))
title_label.pack(pady=10)


name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()
update_button.config(state=tk.DISABLED)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack()

contact_list = tk.Listbox(root)
contact_list.pack()
contact_list.bind("<<ListboxSelect>>", on_contact_select)

root.mainloop()

