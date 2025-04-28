def swap_first_last(letter):
    if len(letter) <= 1:
        return letter
    return letter[-1] + letter[1:-1] + letter[0]


def merge_and_swap(string1, string2):
    swapped_str1 = swap_first_last(string1)
    swapped_str2 = swap_first_last(string2)
    return f"{swapped_str1} {swapped_str2}"