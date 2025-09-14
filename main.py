import sys
from stats import get_char_counts, chars_dict_to_sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_counts = get_char_counts(text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")

    print("============= END ===============")

main()
