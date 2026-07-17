# Decode Function
def decode(code, code_to_letter):

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