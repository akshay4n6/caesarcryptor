import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt_message():
    message = plaintext_entry.get()
    try:
        shift = int(shift_entry.get())
        if shift < 0 or shift > 25:
            raise ValueError("Shift value must be between 0 and 25.")
        encrypted_message = caesar_cipher(message, shift)
        ciphertext_entry.delete(0, tk.END)
        ciphertext_entry.insert(0, encrypted_message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def decrypt_message():
    message = ciphertext_entry.get()
    try:
        shift = int(shift_entry.get())
        if shift < 0 or shift > 25:
            raise ValueError("Shift value must be between 0 and 25.")
        decrypted_message = caesar_cipher(message, -shift)
        plaintext_entry.delete(0, tk.END)
        plaintext_entry.insert(0, decrypted_message)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def clear_fields():
    plaintext_entry.delete(0, tk.END)
    ciphertext_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Text Encryption Tool by Akshay")
root.configure(bg="#1e1e1e")  # Set background color for dark mode

# Define font settings
font_style = ("Arial", 14)

# Create labels and entry widgets with dark mode
tk.Label(root, text="Plaintext:", bg="#1e1e1e", fg="white", font=font_style).grid(row=0, column=0, padx=5, pady=5, sticky="w")
plaintext_entry = tk.Entry(root, font=font_style, bg="#2d2d2d", fg="white", insertbackground="white")
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Ciphertext:", bg="#1e1e1e", fg="white", font=font_style).grid(row=1, column=0, padx=5, pady=5, sticky="w")
ciphertext_entry = tk.Entry(root, font=font_style, bg="#2d2d2d", fg="white", insertbackground="white")
ciphertext_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Shift (0-25):", bg="#1e1e1e", fg="white", font=font_style).grid(row=2, column=0, padx=5, pady=5, sticky="w")
shift_entry = tk.Entry(root, font=font_style, bg="#2d2d2d", fg="white", insertbackground="white")
shift_entry.grid(row=2, column=1, padx=5, pady=5)

# Create buttons for encryption, decryption, and clearing with dark mode
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, font=font_style, bg="#007acc", fg="white", activebackground="#005f91", activeforeground="white")
encrypt_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, font=font_style, bg="#007acc", fg="white", activebackground="#005f91", activeforeground="white")
decrypt_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

clear_button = tk.Button(root, text="Clear", command=clear_fields, font=font_style, bg="#007acc", fg="white", activebackground="#005f91", activeforeground="white")
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Run the main loop
root.mainloop()
