from pathlib import Path


def get_available_codebooks():
    codebooks_folder = Path("codebooks")

    available_codebooks = []

    for file in codebooks_folder.glob("*.json"):
        available_codebooks.append(file.name)

    return available_codebooks