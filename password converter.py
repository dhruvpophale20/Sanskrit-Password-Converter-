import random
import asyncio
from googletrans import Translator
from indic_transliteration.sanscript import transliterate, DEVANAGARI, ITRANS

TRANSLATOR = Translator()

SPECIAL_CHARS = ["@", "#", "%", "&", "*", "!", "$", "^", "_", "-", "+", "=", "~", ":", ";", "<", ">"]


async def generate_password(english_word: str, numbers: str):
    try:
        # Step 1: Translate (await required)
        result = await TRANSLATOR.translate(english_word.strip(), dest="hi")
        devanagari = result.text

        # Step 2: Transliterate
        iast = transliterate(devanagari, DEVANAGARI, ITRANS)

        # Step 3: Symbol
        symbol = random.choice(SPECIAL_CHARS)

        # Step 4: Random order
        permutations = [
            [1, 2, 3], [1, 3, 2],
            [2, 1, 3], [2, 3, 1],
            [3, 1, 2], [3, 2, 1]
        ]
        order = random.choice(permutations)

        parts = {1: symbol, 2: numbers, 3: iast}
        password = "".join(parts[pos] for pos in order)

        return password, devanagari, iast

    except Exception as e:
        return None, None, f"Error: {str(e)}"


def validate_input(word: str, numbers: str):
    if not word.strip():
        return "Word cannot be empty."
    if not word.isalpha():
        return "Word must contain only letters."
    if not numbers.strip():
        return "Numbers cannot be empty."
    if not numbers.isdigit():
        return "Numbers must contain only digits."
    if len(numbers) < 4:
        return "Enter at least 4 digits."
    return None


def get_user_input():
    word = input("Enter an English word: ").strip()
    nums = input("Enter numbers (min 4 digits): ").strip()

    error = validate_input(word, nums)
    if error:
        print(f"Invalid input: {error}")
        return None

    return word, nums


async def main():
    print("=== Sanskrit Password Generator ===\n")

    user_input = get_user_input()
    if not user_input:
        return

    word, nums = user_input

    password, devanagari, iast = await generate_password(word, nums)

    if password:
        print("\n" + "=" * 40)
        print(f"English Word:          {word}")
        print(f"Devanagari:            {devanagari}")
        print(f"IAST (Roman):          {iast}")
        print(f"Generated Password:    {password}")
        print("=" * 40)
    else:
        print(f"\nFailed: {iast}")


# Run async main
if __name__ == "__main__":
    asyncio.run(main())