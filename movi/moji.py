
import ffmpeg
import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog

def transcribe_video():
    # ファイル選択ダイアログを表示して動画ファイルを選択
    file_path = filedialog.askopenfilename(title="動画ファイルを選択",
                                           filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
    
    if not file_path:
        return

    stream = ffmpeg.input(file_path)
    output_file = "output.wav"
    stream = ffmpeg.output(stream, output_file)
    ffmpeg.run(stream)

    r = sr.Recognizer()
    with sr.AudioFile("/Users/amit/Desktop/mojiokosi_AI/test.wav") as source:
        audio = r.record(source)
    text = r.recognize_google(audio, language='ja-JP')
    print(text)

root = tk.Tk()
root.title("動画文字起こし")

btn = tk.Button(root, text="動画ファイルを選択して文字起こし", command=transcribe_video)
btn.pack(pady=20)

root.mainloop()