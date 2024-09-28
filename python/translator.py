import sys

# Define the Braille dictionary for letters a-z and numbers 0-9
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO', ' ': '......',  # Space character
    '1': '.O.....', '2': '.O.O...', '3': '.OO....', '4': '.OO.O..', '5': '.O..O..',
    '6': '.OOO...', '7': '.OOOO..', '8': '.O.OO..', '9': '..OO...', '0': '..OOO..',
    'capital': '.....O',  # Braille symbol for capital letter indicator
    'number': '.OOO.O',    # Braille symbol for number indicator
    'numeric_indicator': 'OOO.OO'  # Braille symbol for numeric indicator (dots 3-4-5-6)
}

# Reverse dictionary for Braille to English
english_from_braille = {v: k for k, v in braille_alphabet.items()}

# Translate English to Braille
def english_to_braille(text):
    translated = []

    for char in text:
        if char.isupper():  # Check for capital letters
            translated.append(braille_alphabet['capital'])  # Add capital letter indicator
            char = char.lower()  # Convert to lowercase for translation
        
        if char.isdigit():  # Check for digits
            translated.append(braille_alphabet['numeric_indicator'])  # Add numeric indicator
            translated.append(braille_alphabet[char])  # Add Braille representation of the digit
        elif char in braille_alphabet:
            translated.append(braille_alphabet[char])
        else:
            translated.append('??????')  # For unknown characters

    return ''.join(translated)

# Translate Braille to English
def braille_to_english(braille):
    translated = []
    is_capital = False
    is_number = False

    # Process the Braille input in chunks of 6 characters
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i + 6]  # Take 6 characters at a time

        if braille_char == braille_alphabet['capital']:
            is_capital = True
            continue
        if braille_char == braille_alphabet['numeric_indicator']:
            is_number = True
            continue

        # Check if the Braille character exists in the reverse dictionary
        if braille_char in english_from_braille:
            char = english_from_braille[braille_char]
            if is_capital:
                char = char.upper()  # Capitalize the character
                is_capital = False  # Reset after using
            if is_number:
                # Convert the first ten letters (a-j) to numbers (1-0)
                if char in 'abcdefghij':
                    char = str('abcdefghij'.index(char) + 1)  # a=1, b=2, ..., j=0
                is_number = False  # Reset after using
            translated.append(char)
        else:
            translated.append('?')  # For unknown characters
            
    return ''.join(translated)

# Main function that handles input and output
def braille_translator(input_str):
    # Determine if input is Braille (all characters are '.' or 'O')
    if all(char in '.O' for char in input_str):
        result = braille_to_english(input_str)  # Translate from Braille to English
        print(result)
    else:
        result = english_to_braille(input_str)  # Translate from English to Braille
        print(result)

# Check if the user provided a command-line argument
if len(sys.argv) == 2:
    input_str = sys.argv[1]  # Take input from command line
else:
    input_str = input("Please enter text or Braille: ")  # Otherwise, prompt for input

# Run the translator with the given input
braille_translator(input_str)

