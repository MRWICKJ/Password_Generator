import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

def password_generator(length: int, use_letters: bool, use_numbers: bool, use_symbols: bool) -> str:
    password_set = ''
    if use_letters:
        password_set += string.ascii_letters
    if use_numbers:
        password_set += string.digits
    if use_symbols:
        password_set += string.punctuation

    if not password_set:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(password_set) for _ in range(length))
    return password

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        password = password_generator(length, use_letters, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)  # Clear previous password
        password_entry.insert(0, password)  # Insert new password
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)  # Copy password to clipboard
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

def run_gui():
    global length_entry, password_entry, letters_var, numbers_var, symbols_var  # Declare global variables

    # Create main window
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x300")
    root.resizable(False, False)

    # Set dark theme colors
    bg_color = "#0e0e0e"  # Dark background
    fg_color = "#ffffff"  # Light foreground

    # Apply dark theme to widgets
    root.configure(bg=bg_color)

    # Title Label
    title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16), bg=bg_color, fg=fg_color)
    title_label.pack(pady=10)

    # Length Label and Entry
    length_label = tk.Label(root, text="Enter password length:", bg=bg_color, fg=fg_color)
    length_label.pack(pady=5)

    length_entry = tk.Entry(root, bg="#1a1a1a", fg=fg_color, insertbackground=fg_color)  # Dark Entry
    length_entry.insert(0, "10")  # Default length
    length_entry.pack(pady=5)

    # Options
    letters_var = tk.BooleanVar(value=True)
    numbers_var = tk.BooleanVar(value=True)
    symbols_var = tk.BooleanVar(value=True)

    letters_check = tk.Checkbutton(root, text="Include letters", variable=letters_var, bg=bg_color, fg=fg_color, selectcolor=bg_color)
    letters_check.pack(anchor='w', padx=20)

    numbers_check = tk.Checkbutton(root, text="Include numbers", variable=numbers_var, bg=bg_color, fg=fg_color, selectcolor=bg_color)
    numbers_check.pack(anchor='w', padx=20)

    symbols_check = tk.Checkbutton(root, text="Include symbols", variable=symbols_var, bg=bg_color, fg=fg_color, selectcolor=bg_color)
    symbols_check.pack(anchor='w', padx=20)

    # Generate Button
    generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#1a1a1a", fg=fg_color)
    generate_button.pack(pady=5)

    # Password Entry
    password_entry = tk.Entry(root, width=40, bg="#1a1a1a", fg=fg_color, insertbackground=fg_color)  # Dark Entry
    password_entry.pack(pady=5)

    # Copy Button
    copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#1a1a1a", fg=fg_color)
    copy_button.pack(pady=5)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    run_gui()
