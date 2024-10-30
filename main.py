import whisper
from moviepy.editor import VideoFileClip
import os

# Step 1: Check if the MP4 file exists and convert to MP3 if present
mp4_file = "Sample.mp4"
mp3_file = "Sample.mp3"

if os.path.isfile(mp4_file):
    video = VideoFileClip(mp4_file)
    video.audio.write_audiofile(mp3_file, codec='mp3')
    print("MP4 file found and converted to MP3.")
else:
    print("No MP4 file found. Skipping conversion step.")

# Step 2: Load the Whisper model
model = whisper.load_model("turbo")

# Step 3: Transcribe the audio if MP3 file exists
if os.path.isfile(mp3_file):
    result = model.transcribe(mp3_file, verbose=True)
    transcript_text = result["text"]

    # Step 4: Save the transcription to a text file
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(transcript_text)
    print("Transcription completed and saved to out.txt.")
else:
    print("No MP3 file found. Skipping transcription step.")