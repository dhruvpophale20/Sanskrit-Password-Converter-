import random
from googletrans import Translator
from indic_transliteration.sanscript import transliterate, DEVANAGARI, ITRANS

# Global translator instance for converting English to Hindi/Sanskrit
TRANSLATOR = Translator()

# Pool of special characters to randomly include in generated passwords
SPECIAL_CHARS = ["@", "#", "%", "&", "*", "!", "$", "^", "_", "-", "+", "=", "~", ":", ";", "<", ">"]


def generate_password(english_word: str, numbers: str = "1234") -> tuple[str | None, str | None, str | None]:
    """
    Generate a password from an English word using Sanskrit transliteration.

    Process:
        1. Translate English word to Hindi (Devanagari script)
        2. Transliterate Devanagari to IAST (Roman script)
        3. Combine with symbol and numbers in random order

    Args:
        english_word: The English word to translate and transliterate
        numbers: A string of numbers to include in the password

    Returns:
        Tuple of (password, devanagari_form, iast_form) or (None, None, error_message)
    """
    try:
        # Step 1: Translate English word to Hindi/Devanagari
        result = TRANSLATOR.translate(english_word.strip(), dest="hi")
        sanskrit_devanagari = result.text

        # Step 2: Convert Devanagari to IAST (Romanized Sanskrit)
        sanskrit_iast = transliterate(sanskrit_devanagari, DEVANAGARI, ITRANS)

        # Step 3: Pick a random special character
        symbol = random.choice(SPECIAL_CHARS)

        # Define all possible orderings: 1=symbol, 2=numbers, 3=IAST word
        permutations = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        order = random.choice(permutations)  # Randomly select one ordering

        # Map position numbers to their values
        parts = {1: symbol, 2: numbers, 3: sanskrit_iast}

        # Build password by joining parts in the selected order
        password = "".join(parts[pos] for pos in order)
        return password, sanskrit_devanagari, sanskrit_iast

    except Exception as e:
        return None, None, f"Error: {str(e)}"


def validate_input(word: str, numbers: str) -> str | None:
    """
    Validate user input and return error message if invalid.

    Args:
        word: The English word to validate
        numbers: The number string to validate

    Returns:
        Error message string if invalid, None if valid
    """
    if not word or not word.strip():
        return "Word cannot be empty."
    if not word.strip().isalpha():
        return "Word must contain only alphabetic characters."
    if not numbers or not numbers.strip():
        return "Numbers cannot be empty."
    if not numbers.strip().isdigit():
        return "Numbers must contain only digits."
    if len(numbers.strip()) < 4:
        return "Please enter at least 4 digits."
    return None


def get_user_input() -> tuple[str, str] | None:
    """
    Prompt user for input and validate it.

    Returns:
        Tuple of (word, numbers) if valid, None if invalid
    """
    word = input("Enter an English word: ").strip()
    nums = input("Enter numbers to include (min 4 digits): ").strip()

    error = validate_input(word, nums)
    if error:
        print(f"Invalid input: {error}")
        return None

    return word, nums


def main() -> None:
    """Main entry point for the password generator."""
    print("=== Sanskrit Password Generator ===\n")

    # Get and validate user input
    user_input = get_user_input()
    if not user_input:
        return

    word, nums = user_input

    # Generate the password
    password, devanagari, iast = generate_password(word, nums)

    # Display results
    if password:
        print(f"\n{'=' * 35}")
        print(f"English Word:         {word}")
        print(f"Sanskrit (Devanagari): {devanagari}")
        print(f"Sanskrit (IAST):      {iast}")
        print(f"Generated Password:   {password}")
        print(f"{'=' * 35}")
    else:
        print(f"\nFailed to generate password: {iast}")


if __name__ == "__main__":
    main()