def arrange_uppercase_first(word: str) -> str:
    upper = ''.join([char for char in word if char.isupper()])
    lower = ''.join([char for char in word if char.islower()])
    return upper + lower