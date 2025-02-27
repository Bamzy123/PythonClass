def insert_ce(word: str, ce: str = "ce") -> str:
    mid = len(word) // 2
    if len(word) % 2 == 0:
        return word[:mid] + ce + word[mid:]
    else:
        return word + ce