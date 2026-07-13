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


# Generate raw audio samples
def generate_audio_samples(duration):
    samples = int(SAMPLE_RATE * duration)

    audio_data = []

    for i in range(samples):
        t = i / SAMPLE_RATE
        sample = math.sin(2 * math.pi * FREQUENCY * t)
        audio_data.append(sample)

    return audio_data


# Generate silence samples
def generate_silence(duration):
    samples = int(SAMPLE_RATE * duration)

    silence = [0.0] * samples

    return silence


# Generate dot (.) or dash (-) audio as a WAV file
def generate_tone(duration, filename):
    audio_data = generate_audio_samples(duration)

    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)

        for sample in audio_data:
            wav_file.writeframes(
                struct.pack("<h", int(sample * 32767))
            )


# Play dot (.) or dash (-) in real time
def play_tone(duration):
    audio_data = generate_audio_samples(duration)

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
        
        
# Save complete Morse code as a single WAV file
def save_morse_audio(morse_code, filename):
    
    all_audio = []
    
    words = morse_code.split("  ")

    for word_index, word in enumerate(words):
        letters = word.split(" ")

        for letter_index, letter in enumerate(letters):
            for symbol in letter:
                if symbol == ".":
                    all_audio.extend(
                        generate_audio_samples(DOT_DURATION)
                    )
                    all_audio.extend(
                        generate_silence(SYMBOL_GAP)
                    )

                elif symbol == "-":
                    all_audio.extend(
                        generate_audio_samples(DASH_DURATION)
                    )
                    all_audio.extend(
                        generate_silence(SYMBOL_GAP)
                    )
                    
            if letter_index != len(letters) - 1:
                all_audio.extend(
                    generate_silence(LETTER_GAP - SYMBOL_GAP)
                )
        
        if word_index != len(words) - 1:
            all_audio.extend(
                generate_silence(WORD_GAP - SYMBOL_GAP)
            )
                    
    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)                # Mono Audio
        wav_file.setsampwidth(2)                # 16-bit Audio
        wav_file.setframerate(SAMPLE_RATE)      # 44100Hz
        
        for sample in all_audio:
            wav_file.writeframes(
            struct.pack("<h", int(sample * 32767))
            )

if __name__ == "__main__":
    play_morse_audio("...")
    save_morse_audio(".... ..  .... .- ... .... . .-.", "hello.wav")
 
   
# Git shows only the code.
# It doesn't show:

# 13+ pages of calculations
# 9 weird diagrams
# 100+ "What if..." ideas
# Several brain reboots
# The notebook deserves commit access too.