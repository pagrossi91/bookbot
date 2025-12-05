import sys

from stats import get_word_count, get_char_count, sorted_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    filepath = sys.argv[1]
    print(f"============ BOOKBOT ============\
          \nAnalyzing book found at {filepath}...")
    
    book_text = get_book_text(filepath)
    num_words = get_word_count(book_text)
    num_chars = get_char_count(book_text)
    char_list = sorted_chars(num_chars)

    print("============= END ===============")
    return

   
main()

