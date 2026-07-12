import math
import struct
import wave

SAMPLE_RATE = 44100
FREQUENCY = 700
DOT_DURATION = 0.1

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
        
generate_tone(DOT_DURATION, "dot.wav")