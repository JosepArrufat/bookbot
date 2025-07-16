import sys
from stats import get_num_words
from stats import count_characters
from stats import order_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_words = get_book_text(sys.argv[1])
        num_of_words = get_num_words(book_words)
        characters_count = count_characters(book_words)
        ordered_count = order_characters(characters_count)
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_of_words} total words")
        print("--------- Character Count -------")
        for character in ordered_count:
            print(f"{character["char"]}: {character["num"]}")

main()