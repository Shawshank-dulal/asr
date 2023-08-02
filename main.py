import whisper
import subprocess

print(subprocess.run('ffmpeg -i input.mp4 -b:a 256K -vn test.mp3'))



model = whisper.load_model("small")
result = model.transcribe("test.mp3")
print(result["text"])