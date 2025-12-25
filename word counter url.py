from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader
from tkinter import ttk
import string
import requests
from bs4 import BeautifulSoup



def calculate():

   
    # --- User input ---
    filename = fn.get()
    search_word = e2.get().lower()

    # --- GET TEXT FROM WEBPAGE ---
    page = requests.get(filename)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.get_text().lower()


# --- Remove punctuation ---
    for punct in string.punctuation:
        text = text.replace(punct, " ")

# --- Count occurrences ---
    words = text.split()
    count = words.count(search_word)

    r.config(text=f"\nThe word '{search_word}' appears {count} times in {filename}.")



root = Tk()
# Set window size: width x height
root.geometry("500x400")  # 500px wide, 400px tall

# Optional: prevent resizing
root.resizable(False, False)  # disable resize horizontally and vertically


# Title
w = Label(root, text='Word Counter', font=("Arial", 25))
w.pack(pady=10)

# --- File selection frame ---
file_frame = Frame(root)
file_frame.pack(pady=5, fill="x", padx=10)

Label(file_frame, text='Enter url').pack(side="left")
fn = Entry(file_frame, width=40)
fn.pack(side="left", padx=5)

# --- Word entry frame ---
word_frame = Frame(root)
word_frame.pack(pady=5, fill="x", padx=10)

Label(word_frame, text='Enter word').pack(side="left")
e2 = Entry(word_frame, width=20)
e2.pack(side="left", padx=5)

# --- Calculate button ---
button = Button(root, text="Calculate Occurrence", command=calculate)
button.pack(pady=15)

# --- Result label ---
r = Label(root, text="", wraplength=500, justify="left")
r.pack(pady=10)



root.mainloop()