import re


def remove_special_characters(word: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', word)