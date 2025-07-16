
def get_num_words(book_string):
    words_array = book_string.split()
    return len(words_array)

def count_characters(book_string):
    words_array = book_string.split()
    characters_count = {}
    for word in words_array:
        for character in word:
            if character.lower() in characters_count:
                characters_count[character.lower()] += 1
            else:
                characters_count[character.lower()] = 1
    return characters_count