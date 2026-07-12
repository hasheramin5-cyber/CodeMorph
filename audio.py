import math
import struct
import time
import wave

import numpy as np
import sounddevice as sd


SAMPLE_RATE = 44100
FREQUENCY = 700
TIME_UNIT = 0.3

DOT_DURATION = TIME_UNIT
DASH_DURATION = TIME_UNIT * 3

SYMBOL_GAP = TIME_UNIT
LETTER_GAP = TIME_UNIT * 3
WORD_GAP = TIME_UNIT * 7


# Generate dot (.) or dash (-) audio as a WAV file
def generate_tone(duration, filename):
    samples = int(SAMPLE_RATE * duration)

    audio_data = []

    for i in range(samples):
        t = i / SAMPLE_RATE
        sample = math.sin(2 * math.pi * FREQUENCY * t)
        audio_data.append(int(sample * 32767))

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)

        for sample in audio_data:
            wav_file.writeframes(struct.pack("<h", sample))


# Play dot (.) or dash (-) in real time
def play_tone(duration):
    samples = int(SAMPLE_RATE * duration)

    audio_data = []

    for i in range(samples):
        t = i / SAMPLE_RATE
        sample = math.sin(2 * math.pi * FREQUENCY * t)
        audio_data.append(sample)

    audio_data = np.array(audio_data, dtype=np.float32)

    sd.play(audio_data, SAMPLE_RATE)
    sd.wait()


# Play Morse code as audio
def play_morse_audio(morse_code):
    words = morse_code.split("  ")

    for word in words:
        letters = word.split(" ")

        for letter in letters:
            for symbol in letter:
                if symbol == ".":
                    play_tone(DOT_DURATION)
                    time.sleep(SYMBOL_GAP)

                elif symbol == "-":
                    play_tone(DASH_DURATION)
                    time.sleep(SYMBOL_GAP)

            time.sleep(LETTER_GAP)

        time.sleep(WORD_GAP)


if __name__ == "__main__":
    play_morse_audio(".... ..  -...")
 
   
# Git shows only the code.
# It doesn't show:

# 8+ pages of calculations
# 7 weird diagrams
# 100+ "What if..." ideas
# Several brain reboots
# The notebook deserves commit access too.