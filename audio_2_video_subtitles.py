import subprocess
import os

# Define paths to your files
mp3_file = "output_audio_russian.mp3"
output_mp4_file = "output_video_without_subtitles.mp4"
srt_file = r"C:/Users/exute/AI/ai_learning_languages/spanish_russian.srt"  # Path to the SRT file
output_video_file = "output_video_with_subtitles.mp4"

# Full path to ffmpeg (update this path to match your system)
ffmpeg_path = r"C:/Users/exute/Downloads/ffmpeg-2024-08-21-git-9d15fe77e3-full_build/ffmpeg-2024-08-21-git-9d15fe77e3-full_build/bin/ffmpeg.exe"

# Create a temporary blank video (e.g., 1280x720 with a black background)
blank_video_file = "blank_video.mp4"
subprocess.run([
    ffmpeg_path, "-f", "lavfi", "-i", "color=size=1280x720:duration=10:rate=30:color=black",
    "-vf", "format=yuv420p", blank_video_file
])

# Combine the blank video, MP3 audio, and subtitles into a single video file
subprocess.run([
    ffmpeg_path, "-i", blank_video_file, "-i", mp3_file, "-vf", f"subtitles={srt_file}",
    "-c:v", "libx264", "-c:a", "aac", "-strict", "experimental", "-b:a", "192k", "-shortest",
    output_video_file
])

# Clean up the temporary blank video file
os.remove(blank_video_file)

print(f"Video file '{output_video_file}' has been created.")

 

 

