# Sanskrit Password Generator

A Python tool that generates secure, memorable passwords by translating English words to Sanskrit and combining them with symbols and numbers.

## Features

- Translates English words to Hindi/Sanskrit (Devanagari script) via Google Translate
- Converts Devanagari to Romanized Sanskrit (ITRANS)
- Generates unique passwords with random component ordering (6 possible permutations)
- Includes a random special character and your custom numbers
- Input validation for a user-friendly experience

## How It Works

1. You enter an **English word** and a **number string** (min 4 digits)
2. The word is translated to Hindi/Sanskrit (Devanagari)
3. The Devanagari script is transliterated to Roman script (ITRANS)
4. A random special character, your numbers, and the ITRANS word are combined in a random order

**Example:**
```
English Word:    hello
Devanagari:      नमस्ते
IAST (Roman):    namaste
Password:        @namaste1234  (one of 6 possible orderings)
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
Enter numbers (min 4 digits): 5678

========================================
English Word:          light
Devanagari:            प्रकाश
IAST (Roman):          prakaasha
Generated Password:    prakaasha5678&
========================================
```

## Password Structure

Each password contains **three components** arranged in one of **six random orderings**:

| Component | Description |
|-----------|-------------|
| **Symbol** | Random character from `@ # $ % & * ! ^ _ - + = ~ : ; < >` |
| **Numbers** | Your custom digit string |
| **ITRANS Word** | Romanized Sanskrit transliteration of your word |

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `googletrans` | `4.0.0-rc1` | English → Hindi translation |
| `indic_transliteration` | latest | Devanagari ↔ ITRANS conversion |

## License

MIT
