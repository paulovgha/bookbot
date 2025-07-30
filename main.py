from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters

def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_characters = sort_characters(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()