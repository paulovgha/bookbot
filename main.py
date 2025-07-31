import sys
from stats import get_num_words, get_num_characters, sort_characters

USAGE_MESSAGE = "Usage: python3 main.py <path_to_book>"

def get_book_text(filepath: str) -> str:
    """Reads and returns the content of a text file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def print_report(book_path: str, word_count: int, sorted_characters: list) -> None:
    """Prints the full analysis report to the console."""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

def main() -> None:
    if len(sys.argv) != 2:
        print(USAGE_MESSAGE)
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    word_count = get_num_words(book_text)
    char_counts = get_num_characters(book_text)
    sorted_characters = sort_characters(char_counts)

    print_report(book_path, word_count, sorted_characters)

if __name__ == "__main__":
    main()