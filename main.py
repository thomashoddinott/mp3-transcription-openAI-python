import whisper

model = whisper.load_model("base")
result = model.transcribe("Sample.mp3")

with open("out.txt", "w") as f:
    f.write(result["text"])