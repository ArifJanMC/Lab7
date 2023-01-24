import string
import tkinter as tk
import webbrowser
from tkinter import filedialog
from tkinter import messagebox

key_symb = None
key_len = None


def valid_char(text):
    global key_symb
    global key_len
    if not all(c.isalpha() and c.isascii() for c in text):
        key_symb = "key_symb"
        return key_symb
    if len(text) > len(text_entry.get()):
        key_len = "key_len"
        return key_len
    return True


def vigenere_cipher(text, key, mode):
    letters = string.ascii_letters
    letter_dict = {letters[i]: i for i in range(len(letters))}
    text_nums = []
    is_upper = []
    for c in text:
        if c.lower() in letter_dict:
            text_nums.append(letter_dict[c.lower()])
            is_upper.append(c.isupper())
        else:
            text_nums.append(c)
            is_upper.append(None)
    key_nums = [letter_dict[c.lower()] for c in key]
    result = []
    for i, c in enumerate(text_nums):
        if isinstance(c, int):
            if mode == "encrypt":
                result.append(chr(((c + key_nums[i % len(key)]) % 26 + 26) % 26 + 65))
            elif mode == "decrypt":
                result.append(chr(((c - key_nums[i % len(key)]) % 26 + 26) % 26 + 65))
        else:
            result.append(c)
    output = []
    for i, c in enumerate(result):
        if is_upper[i] is None:
            output.append(c)
        elif is_upper[i]:
            output.append(c.upper())
        else:
            output.append(c.lower())
    return "".join(output)


def on_select_type():
    if var.get() == "text":
        text_entry.config(state="normal")
        text_browse.config(state="disable")
        key_entry.config(state="normal")
        key_browse.config(state="disable")
    elif var.get() == "file":
        text_entry.config(state="normal")
        text_browse.config(state="normal")
        key_entry.config(state="normal")
        key_browse.config(state="normal")


def on_text_browse():
    filepath = filedialog.askopenfilename()
    if not filepath.endswith('.txt'):
        messagebox.showerror("Error", "Invalid file type. \nPlease select a plaintext file with .txt extension")
        return
    try:
        with open(filepath, 'r') as f:
            text = f.read()
            text_entry.delete(0, tk.END)
            text_entry.insert(0, text)
    except FileNotFoundError:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: file not found.")


def on_key_browse():
    filepath = filedialog.askopenfilename()
    if not filepath.endswith('.txt'):
        messagebox.showerror("Error", "Invalid file type. \nPlease select a plaintext file with .txt extension")
        return
    try:
        with open(filepath, 'r') as f:
            key = f.read()
            key_entry.delete(0, tk.END)
            key_entry.insert(0, key)
    except FileNotFoundError:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: file not found.")


def open_web(event=None):
    webbrowser.open("https://students.vvsu.ru/education/stud/161497/Gasanov_Arif_Shakhievich")


def on_encrypt():
    global result_text
    text = text_entry.get()
    key = key_entry.get()
    if valid_char(key) == "key_symb":
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        messagebox.showerror("Error", "Key contains invalid characters.")
        # result_text.insert(tk.END, "Error: key contains invalid characters.")
    elif valid_char(key) == "key_len":
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        messagebox.showerror("Error", "Key is longer than a text.")
        # result_text.insert(tk.END, "Error: key is longer than a text")
    elif len(key) == 0:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        messagebox.showerror("Error", "Key can't be empty.")
    else:
        result = vigenere_cipher(text, key, "encrypt")
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)


def on_decrypt():
    global result_text
    text = text_entry.get()
    key = key_entry.get()
    if valid_char(key) == "key_symb":
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        messagebox.showerror("Error", "Key contains invalid characters.")
        # result_text.insert(tk.END, "Error: key contains invalid characters.")
    elif valid_char(key) == "key_len":
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        messagebox.showerror("Error", "Key is longer than a text.")
        # result_text.insert(tk.END, "Error: key is longer than a text")
    elif len(key) == 0:
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        messagebox.showerror("Error", "Key can't be empty.")
    else:
        result = vigenere_cipher(text, key, "decrypt")
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, result)


# Create a Tkinter root window
root = tk.Tk()
# Set title of the window and its size
root.title("Vigenere Cipher GUI")
root.geometry("420x600")

# Create a StringVar object and set the default value of it
var = tk.StringVar()
var.set("text")

# Create a Label widget for text label and pack it
text_label = tk.Label(root, text="Enter the text to be encrypted/decrypted:")
text_label.pack()

# Create a Entry widget for text entry and pack it
text_entry = tk.Entry(root, state="normal")
text_entry.pack()

# Create a browse button for text
text_browse = tk.Button(root, text="Browse Text", state="disable", command=on_text_browse)
text_browse.pack()

# Create a label widget for ket label
key_label = tk.Label(root, text="Enter the key for encryption/decryption:")
key_label.pack()

# Create a Entry widget for key entry and pack it
key_entry = tk.Entry(root, state="normal")
key_entry.pack()

# Create a browse button for key
key_browse = tk.Button(root, text="Browse Key", state="disable", command=on_key_browse)
key_browse.pack()

# Create a label to choose the mode
type_label = tk.Label(root, text="Type:")
type_label.pack()

# Create a text mode button
text_type = tk.Radiobutton(root, text="Text", variable=var, value="text", command=on_select_type)
text_type.pack()

# Create a file mode button
file_type = tk.Radiobutton(root, text="File", variable=var, value="file", command=on_select_type)
file_type.pack()

# Create a Label widget for result label and pack it
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Create a Text widget for result and pack it
result_text = tk.Text(root, state="disable", height=10, width=50)
result_text.pack()

# Create a button for encryption and pack it
encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.pack(pady=5)

# Create a button for decryption and pack it
decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.pack()

# Create a button for opening website and pack it
web_button = tk.Button(root, text="ArifJan", command=open_web)
web_button.pack(pady=60)

# Run the Tkinter event loop
root.mainloop()
