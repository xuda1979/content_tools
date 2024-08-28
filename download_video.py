import yt_dlp

def download_youtube_video(video_url, save_path=None):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Combine best video and best audio
        'merge_output_format': 'mp4',          # Ensure the output is in mp4 format
        'outtmpl': save_path + '/%(title)s.%(ext)s' if save_path else '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    video_url = "https://vm.tiktok.com/ZMr3vDyss"
    save_path = None  # Use current directory
    download_youtube_video(video_url, save_path)

