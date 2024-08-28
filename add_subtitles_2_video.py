import os

def get_file_path(prompt_message, file_type):
    file_path = input(f"Enter the path to the {file_type} ({prompt_message}): ").strip()
    return file_path.replace("\\", "/")

def main():
    srt_file = get_file_path("SRT file", "SRT file")
    mp4_file = get_file_path("MP4 file", "MP4 file")
    final_video_file = get_file_path("final output video file", "output MP4 file")
    
    if not srt_file or not mp4_file or not final_video_file:
        print("Error: Please provide all required file paths.")
        return
    
    # Construct the command
    command = f'ffmpeg -i "{mp4_file}" -vf subtitles="{srt_file}" -c:v libx264 -c:a aac -b:a 192k "{final_video_file}"'
    
    # Run the command
    exit_code = os.system(command)
    
    if exit_code == 0:
        print(f"Success: Final video with subtitles has been created: '{final_video_file}'")
    else:
        print("Error: An error occurred during the video processing. Please check your inputs and try again.")

if __name__ == "__main__":
    main()


