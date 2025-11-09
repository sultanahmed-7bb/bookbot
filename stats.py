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
    count_report = ""
    for char in alphabet:
        count = text.lower().count(char)
        chars[char] = count
        count_report += f"{char}: {count}\n" 
    print(count_report)

def report(file_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing file found at {file_path}...")
    print("----------- Word Count ----------")
    word_count(file_path)
    print("--------- Character Count -------")
    char_count(file_path)
    print("============== END ==============")

