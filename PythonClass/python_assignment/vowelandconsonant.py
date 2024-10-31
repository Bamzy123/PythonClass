import re

letter = input("enter a letter: ")

if len(letter) == 1:
    if re.match("[a-zA-Z]+", letter):
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            print(f"{letter} is a vowel letter")
        else:
            print(f"{letter} is a consonant letter")
    else:
        print(f"{letter} is an integer")
else:
    print("length is more than one")