import tkinter as tk
from tkinter import filedialog, messagebox
from googletrans import Translator
import logging
import time
import httpx

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def select_file():
    global input_file_path
    input_file_path = filedialog.askopenfilename(
        title="Select the SRT file",
        filetypes=[("SRT files", "*.srt")]
    )
    if input_file_path:
        file_label.config(text=f"Selected file: {input_file_path}")
        logging.info(f"Selected file: {input_file_path}")
    else:
        file_label.config(text="No file selected")

def translate_srt():
    if not input_file_path:
        messagebox.showerror("Error", "No file selected.")
        return

    # Get the selected languages
    source_language = source_language_var.get()
    target_language = target_language_var.get()

    # Manually set the timeout using httpx.Timeout
    timeout = httpx.Timeout(10.0)

    # Initialize the translator with a manually set timeout
    translator = Translator()

    # Read the SRT file content and parse it into structured blocks
    subtitles = []
    with open(input_file_path, "r", encoding="utf-8") as file:
        block = {}
        for line in file:
            line = line.strip()
            if not line:
                if block:
                    subtitles.append(block)
                    logging.info(f"Parsed subtitle block: {block}")
                    block = {}
            elif '-->' in line:
                block['timestamp'] = line
            elif line.isdigit():
                block['index'] = line
            else:
                block['text'] = block.get('text', '') + line.strip() + ' '  # Combine and strip each line
        if block:
            subtitles.append(block)
            logging.info(f"Parsed subtitle block: {block}")

    # Translate each subtitle block and combine original + translated text
    for subtitle in subtitles:
        if 'text' in subtitle:
            original_text = subtitle['text'].strip()
            translation = translator.translate(original_text, src=source_language, dest=target_language)
            translated_text = translation.text
            combined_text = f"{original_text}\\N{translated_text}"
            subtitle['combined_text'] = combined_text
            logging.info(f"Translated: {original_text} -> {translated_text}")
            time.sleep(1)  # Short delay to prevent rate limiting
        else:
            subtitle['combined_text'] = "[No Text to Translate]"
            logging.warning(f"No text found to translate for subtitle: {subtitle}")

    # Open file dialog to save the output SRT file
    output_file_path = filedialog.asksaveasfilename(
        title="Save Translated SRT",
        defaultextension=".srt",
        filetypes=[("SRT files", "*.srt")],
        initialfile="Translated_with_Chinese.srt"
    )
    
    if not output_file_path:
        messagebox.showerror("Error", "No save location selected.")
        return

    # Write the combined content to the new SRT file
    with open(output_file_path, "w", encoding="utf-8") as translated_file:
        for subtitle in subtitles:
            if 'index' in subtitle and 'timestamp' in subtitle:
                translated_file.write(f"{subtitle['index']}\n")
                translated_file.write(f"{subtitle['timestamp']}\n")
                translated_file.write(f"{subtitle.get('combined_text', '[Translation Error]')}\n\n")
                logging.info(f"Written subtitle block to file: {subtitle}")
            else:
                logging.error(f"Missing index or timestamp in subtitle: {subtitle}")

    messagebox.showinfo("Success", f"Translated SRT file saved to: {output_file_path}")
    logging.info(f"Translated SRT file saved to: {output_file_path}")

# Create the main application window with larger size
root = tk.Tk()
root.title("SRT Translator")
root.geometry("500x400")  # Set the window size to 500x400 pixels

# Label to show selected file
file_label = tk.Label(root, text="No file selected", font=("Arial", 10))
file_label.pack(pady=10)

# Button to select file
select_button = tk.Button(root, text="Select SRT File", command=select_file, font=("Arial", 12))
select_button.pack(pady=10)

# Create dropdown menus for language selection
source_language_var = tk.StringVar(value="es")  # Default to Spanish
target_language_var = tk.StringVar(value="zh-cn")  # Default to Chinese

source_language_label = tk.Label(root, text="Select Source Language:", font=("Arial", 12))
source_language_label.pack(pady=10)
source_language_menu = tk.OptionMenu(root, source_language_var, "es", "en", "fr", "de", "ja", "ko", "ru", "it")
source_language_menu.pack(pady=10)

target_language_label = tk.Label(root, text="Select Target Language:", font=("Arial", 12))
target_language_label.pack(pady=10)
target_language_menu = tk.OptionMenu(root, target_language_var, "zh-cn", "es", "en", "fr", "de", "ja", "ko", "ru", "it")
target_language_menu.pack(pady=10)

# Create a button to trigger the translation
translate_button = tk.Button(root, text="Translate and Save SRT", command=translate_srt, font=("Arial", 14))
translate_button.pack(pady=20)  # Add padding around the button for a better layout

# Run the application
root.mainloop()
