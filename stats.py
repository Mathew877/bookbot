def count_words(text):
    word_list = text.split()
    return len(word_list)


def count_characters(text):
    characters = {}
    for c in text:
        c = c.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters


def sort_on(dict):
    return dict["count"]


def sort_characters(char_dict):
    list_of_chars = []
    for c in char_dict:
        c_dict = { "character":c, "count":char_dict[c]}
        list_of_chars.append(c_dict)
    
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
