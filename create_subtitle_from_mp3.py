import os
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
from datetime import timedelta

# Set the paths to ffmpeg explicitly
ffmpeg_path = r"C:\Users\exute\Downloads\ffmpeg-2024-08-21-git-9d15fe77e3-full_build\ffmpeg-2024-08-21-git-9d15fe77e3-full_build\bin\ffmpeg.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Function to convert milliseconds to SRT time format
def format_timestamp(milliseconds):
    delta = timedelta(milliseconds=milliseconds)
    time_str = str(delta)
    if delta.microseconds:
        time_str = time_str[:-3] + "," + time_str[-3:]
    return time_str.zfill(12).replace(".", ",")

# Convert MP3 to WAV using pydub
def convert_mp3_to_wav(mp3_file, wav_file):
    print(f"Converting {mp3_file} to {wav_file}...")
    audio = AudioSegment.from_mp3(mp3_file)
    audio.export(wav_file, format="wav")
    print("Conversion complete.")

# Recognize speech in the WAV file and create subtitles
def recognize_speech_and_create_srt(wav_file, srt_file):
    recognizer = sr.Recognizer()
    subtitles = []

    print(f"Processing WAV file: {wav_file}")
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)

        try:
            # Recognize the entire content in one go
            text = recognizer.recognize_google(audio, language="ru-RU")

            # Split the text into sentences (basic split by '. ')
            sentences = text.split('. ')

            # Create subtitles entries
            for i, sentence in enumerate(sentences):
                start_time = format_timestamp(i * 1000)  # Assuming 1-second per sentence for demo purposes
                end_time = format_timestamp((i + 1) * 1000)
                subtitles.append(f"{i + 1}\n{start_time} --> {end_time}\n{sentence}\n\n")

        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    # Save the subtitles to an SRT file
    with open(srt_file, "w", encoding="utf-8") as f:
        f.writelines(subtitles)

    print(f"Subtitles saved to {srt_file}")

def main():
    mp3_file = "output_audio_russian.mp3"
    wav_file = "output_audio_russian.wav"
    srt_file = "subtitles.srt"

    # Convert MP3 to WAV
    convert_mp3_to_wav(mp3_file, wav_file)

    # Recognize speech from the WAV file and create subtitles
    recognize_speech_and_create_srt(wav_file, srt_file)

if __name__ == "__main__":
    main()

