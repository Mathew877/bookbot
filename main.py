from stats import count_words, count_characters, sort_characters


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    character_counts = count_characters(text)
    character_lists = sort_characters(character_counts)
    print_book_report(book_path, num_words, character_lists)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def print_book_report(book_path, num_words, character_lists):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c_dict in character_lists:
        char_item = c_dict["character"]
        char_count = c_dict["count"]
        if char_item.isalpha():
            print(F"{char_item}: {char_count}")
    print ("============= END ===============")


main()