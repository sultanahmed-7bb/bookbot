from pathlib import Path

def get_book_text(file_path):
    abs_path = Path(__file__).parent / file_path
    with abs_path.open() as f:
        file_contents = f.read()
    print(file_contents)

def main():
    get_book_text("books/frankenstein.txt")

if __name__ == "__main__":
    main()
