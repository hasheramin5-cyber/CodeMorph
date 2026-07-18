import tkinter as tk


def play_morse_light(encoded_message):
    window = tk.Tk()
    window.title("CodeMorph Signaling")
    window.configure(bg="white")
    window.geometry("400x400+300+150")
    window.attributes("-fullscreen", True)
    window.mainloop()
  
def flash_dot():
    pass

def flash_dash():
    pass

def pause():
    pass

play_morse_light("...")