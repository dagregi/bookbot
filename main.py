def read_file(book_path):
    book = open(book_path, "r")
    text = book.read()
    book.close()

    return text


def get_word_count(text):
    word_list = text.split()
    return len(word_list)


def get_character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def placeholder(character_dict):
    ch_list = []

    for c in character_dict:
        if c.isalpha():
            ch_list.append({"char": c, "count": character_dict[c]})

    ch_list.sort(reverse=True, key=sort_on)
    return ch_list


def sort_on(dict):
    return dict["count"]


def main():
    book_path = "books/frankenstein.txt"
    book = read_file(book_path)
    word_count = get_word_count(book)
    char_list = placeholder(get_character_count(book))

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for item in char_list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")


main()
