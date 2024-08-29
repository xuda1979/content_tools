import yt_dlp
import argparse
import os

def download_youtube_video(video_url, save_path=None):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Combine best video and best audio
        'merge_output_format': 'mp4',          # Ensure the output is in mp4 format
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s') if save_path else '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download video from YouTube or other supported sites.")
    parser.add_argument("video_url", help="The URL of the video to download")
    parser.add_argument("--save_path", help="The directory to save the downloaded video", default=None)

    args = parser.parse_args()
    
    download_youtube_video(args.video_url, args.save_path)


