
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

def order_characters(characters_count):
    def sort_on(items):
        return items["num"]
    ordered_count = []
    for character in characters_count:
        ordered_count.append({"char": character, "num":characters_count[character]})
    ordered_count.sort(reverse=True, key=sort_on)
    return ordered_count

