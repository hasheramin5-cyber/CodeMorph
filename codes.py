import json
from pathlib import Path


def load_codebook(filename="default.json"):
    codebook_path = Path("codebooks") / filename

    with open(codebook_path, "r") as file:
        return json.load(file)


def validate_codebook(letter_to_codes):
    if not letter_to_codes:
        raise ValueError("Codebook is empty.")

    seen_codes = set()

    for letter, codes in letter_to_codes.items():

        if not isinstance(codes, list):
            raise TypeError(
                f"Invalid code list for '{letter}'. Expected a list."
            )

        if not codes:
            raise ValueError(
                f"No codes defined for '{letter}'."
            )

        for code in codes:

            if not isinstance(code, str):
                raise TypeError(
                    f"Invalid code for '{letter}'. Every code must be a string."
                )

            if code in seen_codes:
                raise ValueError(
                    f"Duplicate code '{code}' found for '{letter}'."
                )

            seen_codes.add(code)


def build_reverse_dictionary(letter_to_codes):
    code_to_letter = {}

    for letter, codes in letter_to_codes.items():
        for code in codes:
            code_to_letter[code] = letter

    return code_to_letter


def initialize_codebook(filename="default.json"):
    
    letter_to_codes = load_codebook(filename)
    validate_codebook(letter_to_codes)
    code_to_letter = build_reverse_dictionary(letter_to_codes)

    return letter_to_codes, code_to_letter