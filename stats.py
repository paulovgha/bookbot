from typing import Dict, List

def get_num_words(text: str) -> int:
    """
    Returns the number of words in the given text.
    Splits the text by whitespace.
    """
    return len(text.split())

def get_num_characters(text: str) -> Dict[str, int]:
    """
    Returns a dictionary mapping each character in the text (lowercased)
    to its frequency. Includes all characters: letters, punctuation, spaces, etc.
    """
    character_counts: Dict[str, int] = {}

    for char in text.lower():
        character_counts[char] = character_counts.get(char, 0) + 1

    return character_counts

def sort_characters(char_counts: Dict[str, int]) -> List[Dict[str, int]]:
    """
    Returns a list of dictionaries, each with keys 'char' and 'num',
    sorted in descending order by count.
    Only includes alphabetic characters.
    """
    sorted_characters = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]

    sorted_characters.sort(key=lambda item: item["num"], reverse=True)

    return sorted_characters
