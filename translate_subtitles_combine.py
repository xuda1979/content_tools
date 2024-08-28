import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pysrt
from googletrans import Translator

def translate_subtitles(subtitles, target_languages):
    translator = Translator()
    translations = []
    for sub in subtitles:
        combined_text = sub.text
        for lang in target_languages:
            translated_text = translator.translate(sub.text, dest=lang).text
            combined_text += f"\n[{lang}]: {translated_text}"
        translations.append(combined_text)
    return translations

def create_new_srt(subtitles, translations, output_path):
    new_subtitles = pysrt.SubRipFile()
    for i, sub in enumerate(subtitles):
        new_sub = pysrt.SubRipItem(index=sub.index, start=sub.start, end=sub.end, text=translations[i])
        new_subtitles.append(new_sub)
    
    new_subtitles.save(output_path, encoding='utf-8')

def process_file(input_file, output_file, language_codes):
    subtitles = pysrt.open(input_file, encoding='utf-8')
    translations = translate_subtitles(subtitles, language_codes)
    create_new_srt(subtitles, translations, output_file)
    messagebox.showinfo("Success", f"Translated SRT file saved as {output_file}")

def select_srt_file():
    file_path = filedialog.askopenfilename(title="Select SRT File", filetypes=[("SRT files", "*.srt"), ("All files", "*.*")])
    srt_entry.delete(0, tk.END)
    srt_entry.insert(0, file_path)

def save_srt_file():
    file_path = filedialog.asksaveasfilename(title="Save Translated SRT File As", defaultextension=".srt", filetypes=[("SRT files", "*.srt"), ("All files", "*.*")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def start_translation():
    input_file = srt_entry.get()
    output_file = output_entry.get()
    
    if not input_file or not output_file:
        messagebox.showwarning("Input Error", "Please select the SRT file and set the output file.")
        return

    selected_indices = language_listbox.curselection()
    
    # Correctly map the selected indices to language names and then to language codes
    selected_languages = [language_codes[languages[i]] for i in selected_indices]

    if not selected_languages:
        messagebox.showwarning("Input Error", "Please select at least one language.")
        return

    process_file(input_file, output_file, selected_languages)

# Language options
languages = ["Russian", "Spanish", "French", "German", "Chinese", "Japanese"]
language_codes = {
    "Russian": "ru",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh-cn",
    "Japanese": "ja"
}

# GUI Setup
root = tk.Tk()
root.title("SRT Translator")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

srt_label = tk.Label(frame, text="SRT File:")
srt_label.grid(row=0, column=0, sticky="e")
srt_entry = tk.Entry(frame, width=50)
srt_entry.grid(row=0, column=1, padx=5)
srt_button = tk.Button(frame, text="Browse...", command=select_srt_file)
srt_button.grid(row=0, column=2, padx=5)

output_label = tk.Label(frame, text="Save As:")
output_label.grid(row=1, column=0, sticky="e")
output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=1, column=1, padx=5)
output_button = tk.Button(frame, text="Browse...", command=save_srt_file)
output_button.grid(row=1, column=2, padx=5)

language_label = tk.Label(frame, text="Languages:")
language_label.grid(row=2, column=0, sticky="ne")
language_listbox = tk.Listbox(frame, selectmode="multiple", height=6, exportselection=False)
for language in languages:
    language_listbox.insert(tk.END, language)
language_listbox.grid(row=2, column=1, padx=5)

translate_button = tk.Button(root, text="Translate and Save", command=start_translation, width=30, pady=5)
translate_button.pack(pady=10)

root.mainloop()
