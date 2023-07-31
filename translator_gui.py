import tkinter as tk
from googletrans import Translator

def translate_text():
    source_text = source_text_entry.get()
    target_language = target_language_entry.get()

    translator = Translator()
    translation = translator.translate(source_text, dest=target_language)

    translated_text_entry.delete(5.0, tk.END)
    translated_text_entry.insert(tk.END, translation.text)

def clear_text():
    source_text_entry.delete(0, tk.END)
    target_language_entry.delete(0, tk.END)
    translated_text_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Language Translator")

source_label = tk.Label(root, text="Enter Text:")
source_label.pack()

source_text_entry = tk.Entry(root, width=60 )
source_text_entry.pack()

target_label = tk.Label(root, text="Translate to:")
target_label.pack()

target_language_entry = tk.Entry(root, width=60)
target_language_entry.pack()

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

clear_button = tk.Button(root, text="Clear", command=clear_text)
clear_button.pack()

translated_text_label = tk.Label(root, text="Translated Text:")
translated_text_label.pack()

translated_text_entry = tk.Text(root, width=50, height=20)
translated_text_entry.pack()

root.mainloop()
