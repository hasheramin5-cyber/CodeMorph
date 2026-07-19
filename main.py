from light import play_morse_light
from audio import play_morse_audio, save_morse_audio
from encoder import encode
from decoder import decode

from colorama import init, Fore, Style
init(autoreset=True)

# CodeMorph - Custom Encoder / Decoder

def handle_encode():
    text = input("\nEnter Text: ")
    if not text.strip():
        print(Fore.RED + "\nText cannot be empty.")
        return

    encoded_message = encode(text)

    print(Fore.GREEN + "\nEncoded Message:")
    print(encoded_message)

    play_audio = input("\nPlay Morse Audio? (Y/N): ").upper()

    if play_audio == "Y":
        print(Fore.CYAN + "\nPlaying Morse Audio...")
        play_morse_audio(encoded_message)

    elif play_audio != "N":
        print(Fore.RED + "\nInvalid choice. Audio skipped.")
        
    play_light = input("\nPlay Morse Light? (Y/N): ").upper()

    if play_light == "Y":
        print(Fore.CYAN + "\nPlaying Morse Light...")
        play_morse_light(encoded_message)

    elif play_light != "N":
        print(Fore.RED + "\nInvalid choice. Light skipped.")
        
    save_audio = input("\nSave Morse Audio? (Y/N): ").upper()

    if save_audio == "Y":
        file_name = input("Enter Filename: ")
        file_name = file_name + ".wav"

        save_morse_audio(encoded_message, file_name)

        print(Fore.GREEN + f"\nAudio saved successfully as '{file_name}'")

    elif save_audio != "N":
        print(Fore.RED + "\nInvalid choice. Audio not saved.")
        
        
def handle_decode():
    code = input("\nEnter Code: ")
    if not code.strip():
        print(Fore.RED + "\nCode cannot be empty.")
        return
    
    print(Fore.GREEN + "\nDecoded Message:")
    print(decode(code))
    
    
def show_menu():

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.GREEN + "          CodeMorph v1.0")
    print(Fore.WHITE + "     Custom Encoder / Decoder")
    print(Fore.CYAN + "=" * 45)

    print(Fore.YELLOW + "1. Encode")
    print(Fore.YELLOW + "2. Decode")
    print(Fore.YELLOW + "3. Exit")

    print(Fore.CYAN + "=" * 45)


# Main Program
while True:
  
    show_menu()

    choice = input("Select Option: ")

    if choice == "1":
        handle_encode()

    elif choice == "2":
        handle_decode()

    elif choice == "3":
        print(Fore.GREEN + "\nThank you for using CodeMorph. Goodbye!\n")
        break

    else:
        print(Fore.RED + "\nInvalid Option!\n")