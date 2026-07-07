# 🔐 CodeMorph

> A customizable, Morse code-inspired encoder and decoder built with Python.

CodeMorph is a Python-based encoding and decoding tool inspired by Morse code. Instead of using the standard Morse alphabet, it allows you to define your own symbol mappings, assign multiple codes to the same character, and generate randomized encoded messages while maintaining accurate decoding.

Whether you're learning Python, experimenting with custom communication systems, or exploring basic cryptography concepts, CodeMorph provides a simple and extensible foundation.

---

## ✨ Features

* 🔤 Encode plain text into custom symbols
* 🔓 Decode encoded messages back into text
* 🎲 Randomized encoding using multiple codes per character
* 🛠️ Fully customizable codebook
* 📚 Beginner-friendly and easy to modify
* 🐍 Written entirely in Python
* 🚀 Designed to be expanded with new features

---

## 📂 Project Structure

```text
CodeMorph/
│
├── main.py              # Main application
├── README.md            # Project documentation
├── LICENSE              # MIT License
├── .gitignore           # Git ignored files
└── requirements.txt     # Project dependencies (optional)
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hasheramin5-cyber/CodeMorph.git
```

### 2. Navigate into the project

```bash
cd CodeMorph
```

### 3. Run the program

```bash
python main.py
```

---

## 💻 Example

### Plain Text

```text
HELLO WORLD
```

### Encoded Output

```text
.... . ._.. .-.. ___  .__ --- ._. ._.. _..
```

### Decoded Output

```text
HELLO WORLD
```

> Because multiple codes can be assigned to a single character, the encoded output may be different each time while still decoding correctly.

---

## ⚙️ Customizing the Codebook

Each character can have one or more custom codes.

Example:

```python
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
```

During encoding, CodeMorph randomly selects one of the available codes. During decoding, every valid code maps back to its corresponding character.

---

## 🛣️ Roadmap

Future improvements may include:

* GUI application (Tkinter or CustomTkinter)
* Save and load custom codebooks (JSON)
* Support for numbers and punctuation
* File encoding and decoding
* Password-protected codebooks
* Export encoded messages
* Command-line interface (CLI)
* Unit tests
* Package release on PyPI

---

## 🤝 Contributing

Contributions, ideas, and feature suggestions are welcome.
If you find a bug or have an improvement, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hasher Amin**
Built with Python as part of my software development and open-source learning journey.
