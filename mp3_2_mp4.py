import subprocess

# Define paths to your files
mp3_file = "output_audio_russian.mp3"
output_mp4_file = import tkinter as tk
from tkinter import filedialog, messagebox
import moviepy.editor as mp
import whisper
import os

def generate_srt(video_path, output_srt_path):
    # Extract audio from video
    video = mp.VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    video.audio.write_audiofile(audio_path, codec='pcm_s16le')

    # Transcribe audio using Whisper
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    # Write SRT file
    with open(output_srt_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(result["segments"]):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]

            start_time = whisper.format_timestamp(start, always_include_hours=True)
            end_time = whisper.format_timestamp(end, always_include_hours=True)

            srt_file.write(f"{i + 1}\n{start_time} --> {end_time}\n{text.strip()}\n\n")

    os.remove(audio_path)
    messagebox.showinfo("Success", f"SRT file saved as {output_srt_path}")

def select_video():
    video_file = filedialog.askopenfilename(
        title="Select Video File", 
        filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")]
    )
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_file)

def save_srt():
    srt_file = filedialog.asksaveasfilename(
        title="Save Subtitle File As",
        defaultextension=".srt",
        filetypes=[("SRT files", "*.srt"), ("All files", "*.*")]
    )
    srt_entry.delete(0, tk.END)
    srt_entry.insert(0, srt_file)

def process_video():
    video_file = video_entry.get()
    srt_file = srt_entry.get()
    if not video_file or not srt_file:
        messagebox.showwarning("Input Error", "Please select a video file and specify the subtitle file path.")
        return
    generate_srt(video_file, srt_file)

# GUI Setup
root = tk.Tk()
root.title("SRT Subtitle Generator")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

video_label = tk.Label(frame, text="Video File:")
video_label.grid(row=0, column=0, sticky="e")
video_entry = tk.Entry(frame, width=50)
video_entry.grid(row=0, column=1, padx=5)
video_button = tk.Button(frame, text="Browse...", command=select_video)
video_button.grid(row=0, column=2, padx=5)

srt_label = tk.Label(frame, text="Save As:")
srt_label.grid(row=1, column=0, sticky="e")
srt_entry = tk.Entry(frame, width=50)
srt_entry.grid(row=1, column=1, padx=5)
srt_button = tk.Button(frame, text="Browse...", command=save_srt)
srt_button.grid(row=1, column=2, padx=5)

process_button = tk.Button(root, text="Generate SRT", command=process_video, width=30, pady=5)
process_button.pack(pady=10)

root.mainloop()


# Full path to ffmpeg (update this path to match your system)
ffmpeg_path = r"C:/Users/exute/Downloads/ffmpeg-2024-08-21-git-9d15fe77e3-full_build/ffmpeg-2024-08-21-git-9d15fe77e3-full_build/bin/ffmpeg.exe"

# Convert MP3 to MP4 with a blank video
subprocess.run([
    ffmpeg_path, "-f", "lavfi", "-i", "color=size=1280x720:duration=10:rate=30:color=black",
    "-i", mp3_file, "-c:v", "libx264", "-c:a", "aac", "-b:a", "192k", "-shortest",
    output_mp4_file
])

print(f"MP3 has been converted to MP4: '{output_mp4_file}'")
