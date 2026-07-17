from pathlib import Path


def get_available_codebooks():
    codebooks_folder = Path("codebooks")

    available_codebooks = []

    for file in codebooks_folder.glob("*.json"):
        available_codebooks.append(file.name)

    return available_codebooks

def resolve_codebook_selection(index, available_codebooks):

    index = index - 1

    if index < 0 or index >= len(available_codebooks):
        raise ValueError("Invalid codebook selection.")

    return available_codebooks[index]