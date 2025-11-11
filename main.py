import sys
from stats import word_count
from stats import char_count
from stats import report

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

elif len(sys.argv) == 2:
    file_path = sys.argv[1]

    word_count(file_path)
    
    char_count(file_path)
    
    report(file_path)
