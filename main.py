from codebook_manager import (
    get_available_codebooks,
    resolve_codebook_selection
)
from codes import initialize_codebook
from audio import play_morse_audio, save_morse_audio
from encoder import encode
from decoder import decode

from colorama import init, Fore
init(autoreset=True)


def handle_encode():
    text = input("\nEnter Text: ")

    if not text.strip():
        print(Fore.RED + "\nText cannot be empty.")
        return

    encoded_message = encode(text, letter_to_codes)

    print(Fore.GREEN + "\nEncoded Message:")
    print(encoded_message)

    play_audio = input("\nPlay Morse Audio? (Y/N): ").upper()

    if play_audio == "Y":
        print(Fore.CYAN + "\nPlaying Morse Audio...")
        play_morse_audio(encoded_message)

    elif play_audio != "N":
        print(Fore.RED + "\nInvalid choice. Audio skipped.")

    save_audio = input("\nSave Morse Audio? (Y/N): ").upper()

    if save_audio == "Y":
        file_name = input("Enter Filename: ") + ".wav"

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
    print(decode(code, code_to_letter))


def show_menu(selected_codebook):

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.GREEN + "          CodeMorph v1.0")
    print(Fore.WHITE + "     Custom Encoder / Decoder")
    print(Fore.CYAN + "=" * 45)

    print(Fore.WHITE + f"\nCurrent Codebook: {selected_codebook}")
    print(Fore.YELLOW + "1. Encode")
    print(Fore.YELLOW + "2. Decode")
    print(Fore.YELLOW + "3. Exit")

    print(Fore.CYAN + "=" * 45)


def select_codebook():

    available_codebooks = get_available_codebooks()

    print(Fore.CYAN + "\n" + "=" * 45)
    print(Fore.GREEN + "Available Codebooks")
    print(Fore.CYAN + "=" * 45 + "\n")

    for number, codebook in enumerate(available_codebooks, start=1):
        print(Fore.YELLOW + f"{number}. {codebook}")

    while True:
        try:
            selection = int(input("\nSelect Codebook: "))

            selected_codebook = resolve_codebook_selection(
                selection,
                available_codebooks
            )

            return selected_codebook

        except ValueError:
            print(Fore.RED + "\nInvalid codebook selection.")


selected_codebook = select_codebook()

letter_to_codes, code_to_letter = initialize_codebook(selected_codebook)


while True:

    show_menu(selected_codebook)

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