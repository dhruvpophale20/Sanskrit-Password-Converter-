# Sanskrit Password Generator

A Python tool that generates secure passwords by translating English words to Sanskrit and combining them with symbols and numbers.

## Features

- Translates English words to Hindi/Sanskrit (Devanagari script)
- Converts Devanagari to Romanized Sanskrit (IAST/ITRANS)
- Generates unique passwords with random component ordering
- Includes special characters and custom numbers
- Input validation for user-friendly experience

## How It Works

1. Enter an English word
2. The word is translated to Hindi/Sanskrit
3. The Devanagari script is transliterated to IAST (Roman script)
4. A random special character, your numbers, and the IAST word are combined in random order

**Example:**
```
English Word:    hello
Sanskrit (Dev):  नमस्ते
Sanskrit (IAST): namaste
Password:        @namaste1234  (or any permutation)
```

## Installation

```bash
pip install googletrans==4.0.0-rc1 indic_transliteration
```

## Usage

```bash
python "password converter.py"
```

Then follow the prompts:
- Enter an English word (letters only)
- Enter numbers to include (minimum 4 digits)

## Example Output

```
=== Sanskrit Password Generator ===

Enter an English word: light
Enter numbers to include (min 4 digits): 5678

===================================
English Word:         light
Sanskrit (Devanagari): प्रकाश
Sanskrit (IAST):      prakaasha
Generated Password:   prakaasha5678&
===================================
```

## Password Structure

Each password contains three components:
- **Symbol** - Random character from `@#$%&*!$^_+-=~:;<>`
- **Numbers** - Your custom digit string
- **IAST Word** - Romanized Sanskrit transliteration

The three components are arranged in one of six possible orderings, chosen randomly each time.

## Dependencies

| Package | Purpose |
|---------|---------|
| `googletrans` | English to Hindi translation |
| `indic_transliteration` | Devanagari ↔ IAST conversion |

## License

MIT
