import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)
    
    # Calculate the strength score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_char_criteria:
        feedback.append("Password should contain at least one special character.")
    
    return score, feedback

def assess_password():
    """Assess the password entered by the user and provide feedback."""
    password = password_entry.get()
    score, feedback = check_password_strength(password)
    
    # Display strength feedback
    if score == 5:
        strength_label.config(text="Password Strength: Strong", fg="green")
    elif 3 <= score < 5:
        strength_label.config(text="Password Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Password Strength: Weak", fg="red")
    
    # Display specific feedback
    feedback_text = "\n".join(feedback) if feedback else "Your password is strong!"
    feedback_label.config(text=feedback_text)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place widgets
tk.Label(root, text="Enter Password:").pack(pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=assess_password)
check_button.pack(pady=10)

strength_label = tk.Label(root, text="Password Strength: ", font=("Arial", 12))
strength_label.pack(pady=5)

feedback_label = tk.Label(root, text="", font=("Arial", 10), wraplength=400, justify="left")
feedback_label.pack(pady=10)

# Run the application
root.mainloop()
