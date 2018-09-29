"""
recognize_from_file.py -- recognize from file
"""

import speech_recognition as sr

r = sr.Recognizer()
audiofile = sr.AudioFile('/home/sohnryang/Downloads/OSR_us_000_0010_8k.wav')
with audiofile as source:
    audio = r.record(source)
print(r.recognize_google(audio))
