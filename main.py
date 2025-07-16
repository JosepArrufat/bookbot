from stats import get_num_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
   book_words = get_book_text("books/frankenstein.txt")
   num_of_words = get_num_words(book_words)
   characters_count = count_characters(book_words)
   print(f"{num_of_words} words found in the document")
   print(characters_count)

main()