import tkinter as tk
import time


DOT_TIME = 0.15
DASH_TIME = DOT_TIME * 3

SYMBOL_GAP = DOT_TIME
LETTER_GAP = DOT_TIME * 3
WORD_GAP = DOT_TIME * 7


def play_morse_light(encoded_message):
    window = tk.Tk()
    window.bind("<Escape>", lambda event: window.destroy())
    window.title("CodeMorph Signaling")
    window.configure(bg="black")
    window.attributes("-fullscreen", True)

    window.update()

    i = 0

    while i < len(encoded_message):
        symbol = encoded_message[i]
        
        if symbol == ".":
            flash_dot(window)

        elif symbol in ["-", "_"]:
            flash_dash(window)
            
        elif symbol == " ":
            if i + 1 < len(encoded_message) and encoded_message[i + 1] == " ":
                time.sleep(WORD_GAP - SYMBOL_GAP)
                i += 1
            else:
                time.sleep(LETTER_GAP - SYMBOL_GAP)
            
        i += 1

    time.sleep(0.5)
    window.destroy()


def flash_dot(window):
    window.configure(bg="#FFFFAA")
    window.update()
    time.sleep(DOT_TIME)

    window.configure(bg="black")
    window.update()
    time.sleep(SYMBOL_GAP)


def flash_dash(window):
    window.configure(bg="#FFFFAA")
    window.update()
    time.sleep(DASH_TIME)

    window.configure(bg="black")
    window.update()
    time.sleep(SYMBOL_GAP)