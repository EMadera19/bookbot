def number_of_words(text):
    return len(text.split())

def number_of_character(text):
    character = {}
    for char in text:
        lowercase_character = char.lower()
        if lowercase_character in character:
            character[lowercase_character] += 1
        else:
            character[lowercase_character] = 1
    return character

def sorted_list(character):
    character = list(character.items())
    sorted_characters = sorted(character, key=lambda x: x[1], reverse=True)
    return sorted_characters