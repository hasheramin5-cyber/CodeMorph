from audio import play_morse_audio, save_morse_audio
from encoder import encode
from decoder import decode

# CodeMorph - Custom Encoder / Decoder

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