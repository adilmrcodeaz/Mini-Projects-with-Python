import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password(length=12):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def show_password():
    password_length = int(entry.get())
    password = generate_random_password(password_length)
    messagebox.showinfo("Generated Password", password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create a label and entry for password length
label = tk.Label(root, text="Enter password length:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# Create a button to generate the password
button = tk.Button(root, text="Generate Password", command=show_password)
button.pack(pady=20)

# Run the application
root.mainloop()
