from pathlib import Path

def get_book_text(file_path):
    abs_path = Path(__file__).parent / file_path
    with abs_path.open() as f:
        file_contents = f.read()
    return file_contents

def word_count(file_path):
    book_text = get_book_text(file_path)
    words = book_text.split()
    print(f'Found {len(words)} total words')

def char_count(file_path):
    text = get_book_text(file_path)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    chars = {}
    for char in alphabet:
        count = text.lower().count(char)
        chars[char] = count
    print(chars)

