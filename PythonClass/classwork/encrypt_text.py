def get_encrypt_text(text):
    word = []
    for char in text:
        if 'a' <= char <= 'z':
            word.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            word.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            word.append(char)
    return ''.join(word)