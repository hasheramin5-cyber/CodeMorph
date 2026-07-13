from audio import play_morse_audio
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


# Main Program

while True:
  
    print("\n\nCodeMorph - Encoder/Decoder")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

    choice = input("Select Option: ")

    if choice == "1":
        text = input("\nEnter Text: ")

        encoded_message = encode(text)

        print("\nEncoded Message:\n")
        print(encoded_message)

        play_audio = input("\nPlay Morse Audio? (Y/N): ").upper()

        if play_audio == "Y":
            print("\nPlaying Morse Audio...\n")
            play_morse_audio(encoded_message)

    elif choice == "2":
        code = input("\nEnter Code: ")
        print("\nDecoded Message:\n")
        print(decode(code))

    elif choice == "3":
        print("\nThank you for using CodeMorph!\n")
        break

    else:
        print("\nInvalid Option!\n")