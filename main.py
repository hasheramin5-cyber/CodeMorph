from audio import play_morse_audio, save_morse_audio
import random

# CodeMorph - Custom Encoder / Decoder

# Multiple codes can be assigned to each letter.

letter_to_codes = {
    "A": [".-", "._"],
    "B": ["-...", "_..."],
    "C": ["-.-.", "_._."],
    "D": ["-..", "_.."],
    "E": ["."],
    "F": ["..-.", ".._."],
    "G": ["--.", "__."],
    "H": ["...."],
    "I": [".."],
    "J": [".---", ".___"],
    "K": ["-.-", "_._"],
    "L": [".-..", "._.."],
    "M": ["--", "__"],
    "N": ["-.", "_."],
    "O": ["---", "___"],
    "P": [".--.", ".__."],
    "Q": ["--.-", "__._"],
    "R": [".-.", "._."],
    "S": ["..."],
    "T": ["-", "_"],
    "U": ["..-", ".._"],
    "V": ["...-", "..._"],
    "W": [".--", ".__"],
    "X": ["-..-", "_.._"],
    "Y": ["-.--", "_.__"],
    "Z": ["--..", "__.."],
    "1":[".----" , ".____"],
    "2":["..---" , "..___"],
    "3":["...--" , "...__"],
    "4":["....-" , "...._"],
    "5":["....."],
    "6":["-...." , "_...."],
    "7":["--..." , "__..."],
    "8":["---.." , "___.."],
    "9":["----." , "____."],
    "0":["-----" , "_____"]
}

# Create Reverse Dictionary Automatically
code_to_letter = {}

for letter, codes in letter_to_codes.items():
    for code in codes:
        code_to_letter[code] = letter

# Encode Function

def encode(text):

    words = text.upper().split()
    encoded_words = []

    for word in words:

        encoded_letters = []

        for letter in word:

            if letter in letter_to_codes:

                # Randomly choose one code
                random_code = random.choice(letter_to_codes[letter])

                encoded_letters.append(random_code)

        encoded_words.append(" ".join(encoded_letters))

    return "  ".join(encoded_words)


# Decode Function

def decode(code):

    words = code.strip().split("  ")
    decoded_words = []

    for word in words:

        decoded_letters = []

        for item in word.split():

            decoded_letters.append(
                code_to_letter.get(item, "?")
            )

        decoded_words.append("".join(decoded_letters))

    return " ".join(decoded_words)


def handle_encode():
    text = input("\nEnter Text: ")
    if not text.strip():
        print("\nText cannot be empty.")
        return

    encoded_message = encode(text)

    print("\nEncoded Message:")
    print(encoded_message)

    play_audio = input("\nPlay Morse Audio? (Y/N): ").upper()

    if play_audio == "Y":
        print("\nPlaying Morse Audio...")
        play_morse_audio(encoded_message)

    elif play_audio != "N":
        print("\nInvalid choice. Audio skipped.")
        
    save_audio = input("\nSave Morse Audio? (Y/N): ").upper()

    if save_audio == "Y":
        file_name = input("Enter Filename: ")
        file_name = file_name + ".wav"

        save_morse_audio(encoded_message, file_name)

        print(f"\nAudio saved successfully as '{file_name}'")

    elif save_audio != "N":
        print("\nInvalid choice. Audio not saved.")
        
        
def handle_decode():
    code = input("\nEnter Code: ")
    if not code.strip():
        print("\nCode cannot be empty.")
        return
    
    print("\nDecoded Message:")
    print(decode(code))
    
    
def show_menu():

    print("\n" + "=" * 45)
    print("          CodeMorph v1.0")
    print("     Custom Encoder / Decoder")
    print("=" * 45)

    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

    print("=" * 45)


# Main Program

while True:
  
    show_menu()

    choice = input("Select Option: ")

    if choice == "1":
        handle_encode()

    elif choice == "2":
        handle_decode()

    elif choice == "3":
        print("\nThank you for using CodeMorph!\n")
        break

    else:
        print("\nInvalid Option!\n")