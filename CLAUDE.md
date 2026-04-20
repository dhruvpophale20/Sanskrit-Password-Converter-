# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Sanskrit Password Generator - Converts English words into secure passwords using:
1. English → Hindi/Sanskrit translation (Devanagari script)
2. Devanagari → IAST transliteration (Roman script)
3. Random combination with symbols and numbers

## Running the Application

```bash
python "password converter.py"
```

## Dependencies

- `googletrans` - Google Translate API wrapper for translation
- `indic_transliteration` - Sanskrit transliteration between scripts (Devanagari ↔ ITRANS)

Install:
```bash
pip install googletrans==4.0.0-rc1 indic_transliteration
```

## Code Structure

Single-file application (`password converter.py`) with four functions:

- `generate_password(word, numbers)` - Core logic: translates word to Devanagari, transliterates to IAST, combines with symbol/numbers in random order
- `validate_input(word, numbers)` - Validates input (alphabetic word, digit-only numbers, min 4 digits)
- `get_user_input()` - Interactive prompts with validation
- `main()` - Entry point with formatted output

## Password Format

Password components (symbol, numbers, IAST word) are arranged in one of 6 random permutations. Special characters drawn from 18-character pool.
