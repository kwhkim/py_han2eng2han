from jamo import h2j, j2hcj

# Mapping of Hangul jamo (basic letters) to English keys
hangul_to_english = {
    'ㅂ': 'q', 'ㅃ': 'Q', 'ㅈ': 'w', 'ㅉ': 'W', 'ㄷ': 'e', 'ㄸ': 'E',
    'ㄱ': 'r', 'ㄲ': 'R', 'ㅅ': 't', 'ㅆ': 'T', 'ㅛ': 'y', 'ㅕ': 'u',
    'ㅑ': 'i', 'ㅐ': 'o', 'ㅒ': 'O', 'ㅔ': 'p', 'ㅖ': 'P', 'ㅁ': 'a',
    'ㄴ': 's', 'ㅇ': 'd', 'ㄹ': 'f', 'ㅎ': 'g', 'ㅗ': 'h', 'ㅓ': 'j',
    'ㅏ': 'k', 'ㅣ': 'l', 'ㅋ': 'z', 'ㅌ': 'x', 'ㅊ': 'c', 'ㅍ': 'v',
    'ㅠ': 'b', 'ㅜ': 'n', 'ㅡ': 'm'
}

def convert_hangul_to_english(hangul_text):
    """
    Convert Hangul mis-input to English based on keyboard mapping.
    """
    decomposed = j2hcj(h2j(hangul_text))  # Decompose Hangul syllables into jamo
    english_text = ''.join(hangul_to_english.get(char, char) for char in decomposed)
    return english_text

if __name__ == "__main__":
    print("Hangul to English Converter")
    print("-" * 30)

    while True:
        hangul_input = input("\nEnter mis-inputted Hangul text (or type 'exit' to quit): ")
        if hangul_input.lower() == "exit":
            print("Exiting the converter. Goodbye!")
            break
        correct_text = convert_hangul_to_english(hangul_input)
        print(f"Converted text: {correct_text}")
