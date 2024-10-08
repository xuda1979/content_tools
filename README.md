
# Content Tools

A collection of Python scripts and tools designed to work with content such as subtitles, translations, and other media-related tasks. This repository includes utilities for translating subtitle files, merging translations, and processing video content.

## Features

- **Subtitle Translation**: Translate SRT subtitle files into multiple languages using Google Translate API.
- **Video Processing**: Combine subtitles with video files using FFmpeg.
- **Multi-Language Support**: Translate subtitles into multiple languages simultaneously and save the output in a new SRT file.

## Requirements

Before using the tools, ensure you have the following installed:

- Python 3.x
- `pysrt` - Python library for reading and writing SubRip (SRT) files.
- `googletrans` - Python library for translating text using Google Translate API.
- `ffmpeg` - Command-line tool for processing multimedia files.

You can install the required Python packages using `pip`:

\`\`\`bash
pip install pysrt googletrans==4.0.0-rc1
\`\`\`

Ensure `ffmpeg` is installed and available in your system's PATH. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Usage

### 1. Subtitle Translation Tool

Translate subtitles into multiple languages and save them in a new SRT file.

#### How to Use:

1. Run the `translate_subtitles_combine.py` script.
2. Use the GUI to select the SRT file you want to translate.
3. Choose where to save the translated file.
4. Select one or more languages from the list.
5. Click "Translate and Save" to generate the translated SRT file.

#### Example:

\`\`\`bash
python translate_subtitles_combine.py
\`\`\`

### 2. Video and Subtitle Merging Tool

Combine video files with translated subtitles using FFmpeg.

#### How to Use:

1. Run the `combine_video_subtitles.py` script.
2. Select the video (MP4) and subtitle (SRT) files using the GUI.
3. Choose where to save the final video file.
4. Click "Combine and Save Video" to process and save the output.

#### Example:

\`\`\`bash
python combine_video_subtitles.py
\`\`\`

### 3. Custom FFmpeg Processing

Process videos with custom FFmpeg commands directly from the terminal.

#### Example Command:

\`\`\`bash
ffmpeg -i input.mp4 -vf subtitles=input.srt -c:v libx264 -c:a aac -b:a 192k output.mp4
\`\`\`

## Troubleshooting

### Common Issues:

- **KeyError during translation**: Ensure that the selected languages are correctly mapped in the script. See the `translate_subtitles_combine.py` script for details on how to fix this.
- **Connection errors with Google Translate**: Retry the translation or check your network connection.

### Debugging Tips:

- Use a stable internet connection for translations.
- Ensure that all file paths are correct and that necessary permissions are set.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
