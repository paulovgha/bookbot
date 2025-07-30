def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_characters = {}
    for char in text.lower():
        if char in num_characters:
            num_characters[char] += 1
        else:
            num_characters[char] = 1
    return num_characters

def sort_characters(char_counts):
    sorted_char_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_char_list.append({"char": char, "num": count})

    # Sort from highest to lowest count
    sorted_char_list.sort(key=lambda item: item["num"], reverse=True)

    return sorted_char_list