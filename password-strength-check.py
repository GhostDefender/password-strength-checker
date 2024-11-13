import re
import tkinter as tk
from tkinter import ttk

# Function to evaluate the strength of the password
def password_strength(password):
    score = 0

    # Password criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[\W_]", password) is not None

    # Increase score based on fulfilled criteria
    if length_criteria:
        score += 1
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if digit_criteria:
        score += 1
    if special_criteria:
        score += 1

    # Password strength evaluation
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return score, strength

# Function to update the strength in the interface
def check_password_strength(*args):
    password = password_entry.get()
    score, strength = password_strength(password)
    
    score_label.config(text=f"Score: {score}")
    strength_label.config(text=f"Strength: {strength}")

    # Change color according to strength level
    if strength == "Very Strong":
        strength_label.config(foreground="green")
    elif strength == "Strong":
        strength_label.config(foreground="blue")
    elif strength == "Moderate":
        strength_label.config(foreground="orange")
    else:
        strength_label.config(foreground="red")

# Main window configuration
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")

# Instruction label
instruction_label = ttk.Label(root, text="Enter a password:")
instruction_label.pack(pady=10)

# Password entry field
password_entry = ttk.Entry(root, show="*")
password_entry.pack(pady=5)
password_entry.bind("<KeyRelease>", check_password_strength)  # Calls the function every time a character is entered

# Labels to display score and strength
score_label = ttk.Label(root, text="Score: ")
score_label.pack(pady=5)

# Change ttk.Label to tk.Label for color functionality
strength_label = tk.Label(root, text="Strength: ")
strength_label.pack(pady=5)

# Start the main window
root.mainloop()
