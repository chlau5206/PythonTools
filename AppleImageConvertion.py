""" Apple image HEIC convertion
pre-conditional:
> pip install pyheif pillow

1. Convert HEIC to jpg
2. Convert HEVC to MP4 

Popular Formats for HEIC conversion
-- JPG, PNG, TIFF, GIF, BMP, WEBP, PDF, PSD, ICO, AVIF

Popular Formats for HEVC Conversion
-- MP4, MOV, AVI, MKV, WEBM, GIF, MPEG-2, FLV, WMV, AV1

Choosing the Right Format
    For compatibility: MP4 is the safest choice.
    For high quality: MOV or MKV are excellent options.
    For web use: WEBM is lightweight and efficient. 
    For older systems: AVI or WMV might be better.

"""

import pyheif
from PIL import Image
import os
import subprocess

def convert_heic_to_jpg(input_file, output_file):
    # Open the HEIC file
    heif_file = pyheif.read(input_file)
    # Convert to a PIL Image
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    # Save as JPG
    image.save(output_file, format="JPEG")
    print(f"Converted {input_file} to {output_file}")

"""  Convert HEVC to other formats
#1. Install FFmpeg:
    1.1 Download FFmpeg for Windows from {https://ffmpeg.org/download.html}

#2. Install Required Python Libraries:
    Bash
    $ pip install subprocess    

parameters: 
Convert HEVC to MP4(H.264 + AAC):
    "-c:v", "libx264",     # Video codec set to H.264 (MP4 compatible)
    "-c:a", "aac",         # Audio codec set to AAC (widely supported)

Convert HEVC to AVI:
    "-c:v", "mpeg4",       # Video codec set to MPEG-4 (compatible with AVI)
    "-c:a", "libmp3lame",  # Audio codec set to MP3

Conver HEVC to MKV:
    "-c:v", "libx265",     # Keeps HEVC codec for video
    "-c:a", "aac",         # Audio codec set to AAC

Convert HEVC to MOV:
    "-c:v", "libx264",     # Video codec set to H.264
    "-c:a", "aac",         # Audio codec set to AAC

Convert HEVC to FLV:
    "-c:v", "libx264",     # Video codec set to H.264 (Flash-compatible)
    "-c:a", "aac",         # Audio codec set to AAC

Convert HEVC to WebM:    
    "-c:v", "libvpx-vp9",  # Video codec set to VP9 (WebM-compatible)
    "-c:a", "libvorbis",   # Audio codec set to Vorbis

Bash    
// Basic MKV packaging:
$ ffmpeg -i input.mp4 -c:v copy -c:a copy -c:s copy output.mkv

// Adding Multiple Audio or Subtitle Tracks:
$ ffmpeg -i video.mp4 -i audio1.mp3 -i audio2.aac -map 0:v -map 1:a -map 2:a -c:v copy -c:a copy output.mkv

// Embedding External Subtitles:
$ ffmpeg -i input.mp4 -i subtitles.srt -c:v copy -c:a copy -c:s mov_text output.mkv

"""

def convert_hevc_to_mp4(input_file, output_file):
    # FFmpeg command for Windows
    command = [
        "ffmpeg",
        "-i", input_file,      # Input file
        "-c:v", "libx264",     # Set video codec to H.264
        "-c:a", "aac",         # Set audio codec to AAC
        output_file            # Output file
    ]

    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

def convert_hevc_to_mp4_with_mp3(input_file, output_file):
    # FFmpeg command for converting HEVC to MP4 with MP3 audio codec
    command = [
        "ffmpeg",
        "-i", input_file,      # Input file
        "-c:v", "libx264",     # Video codec set to H.264 (MP4 compatible)
        "-c:a", "libmp3lame",  # Audio codec set to MP3 (requires libmp3lame)
        output_file            # Output file
    ]

    try:
        # Execute the FFmpeg command
        subprocess.run(command, check=True)
        print(f"Conversion successful: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

def batch_convert_hevc_to_mp4(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(input_folder):
        if file_name.endswith(".hevc"):
            os.path.abspath
            input_file = os.path.join(input_folder, file_name)
            output_file = os.path.join(output_folder, file_name.replace(".hevc", ".mp4"))
            command = ["ffmpeg", 
                       "-i", input_file, 
                       "-c:v", "libx264", 
                       "-c:a", "aac", 
                       output_file]
            try:
                subprocess.run(command, check=True)
                print(f"Converted {file_name} to {output_file}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {file_name}: {e}")

# Example usage

if __name__ == '__main__':
    input_folder = os.path.join(os.getcwd(), 'input')
    output_folder = os.path.join(os.getcwd(), 'output')

    input_file = os.path.join(input_folder, 'test.heic')
    output_file = os.path.join(output_folder, 'test.jpg')
    convert_heic_to_jpg(input_file, output_file)

    convert_hevc_to_mp4("input.hevc", "output.mp4")   # aac audio
    convert_hevc_to_mp4_with_mp3("input.hevc", "output.mp4")
    batch_convert_hevc_to_mp4(input_folder, output_folder)

