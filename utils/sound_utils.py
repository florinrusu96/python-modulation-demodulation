import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def record(seconds=3):
    fs = 44100  # Sample rate
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    print(f"Recording for {seconds} seconds")
    sd.wait()  # Wait until recording is finished
    print("Finished recording")
    print(len(myrecording))
    return myrecording

def play(sound):
    fs = 44100  # Sample rate
    sd.play(sound, fs, mapping=[1])
    sd.wait()
    sd.stop()
    