import random

# Encode Function
def encode(text, letter_to_codes):

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