class Book:
    def __init__(self, book_path):
        book = open(book_path, "r")
        self.text = book.read()
        self.word_count = self.get_word_count()
        self.chars = self.get_character_count()
        self.ch_list = self.get_character_list()
        book.close()

    def get_word_count(self):
        word_list = self.text.split()
        return len(word_list)

    def get_character_count(self):
        chars = {}
        for ch in self.text:
            ch_l = ch.lower()
            if ch_l in chars:
                chars[ch_l] += 1
            else:
                chars[ch_l] = 1
        return chars

    def get_character_list(self):
        ch_list = []

        for c in self.chars:
            if c.isalpha():
                ch_list.append({"char": c, "count": self.chars[c]})

        ch_list.sort(reverse=True, key=sort_on)
        return ch_list


def sort_on(dict):
    return dict["count"]


def main():
    book_path = "books/frankenstein.txt"
    book = Book(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{book.word_count} words found in the document\n")
    for item in book.ch_list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")


main()
