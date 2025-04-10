import sys
from stats import number_of_words, number_of_character, sorted_list

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])
    word_count = number_of_words(text)
    character_count = number_of_character(text)
    sorted_characters = sorted_list(character_count)


    print(f"Found {word_count} total words")
    
    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")

main()
