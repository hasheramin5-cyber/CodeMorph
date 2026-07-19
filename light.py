import tkinter as tk
import time


DOT_TIME = 0.15
DASH_TIME = DOT_TIME * 3
GAP_TIME = DOT_TIME


def play_morse_light(encoded_message):
    window = tk.Tk()
    window.bind("<Escape>", lambda event: window.destroy())
    window.title("CodeMorph Signaling")
    window.configure(bg="black")
    window.attributes("-fullscreen", True)

    window.update()

    for symbol in encoded_message:
        if symbol == ".":
            flash_dot(window)

        elif symbol == "-":
            flash_dash(window)

    time.sleep(0.5)
    window.destroy()


def flash_dot(window):
    window.configure(bg="#FFFFAA")
    window.update()
    time.sleep(DOT_TIME)

    window.configure(bg="black")
    window.update()
    time.sleep(GAP_TIME)


def flash_dash(window):
    window.configure(bg="#FFFFAA")
    window.update()
    time.sleep(DASH_TIME)

    window.configure(bg="black")
    window.update()
    time.sleep(GAP_TIME)