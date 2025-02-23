def get_seven_segment_display(digit: int) -> list:

    if digit < 0 or digit > 9:
        raise ValueError("Digit must be between 0 and 9")

    display = [[' ' for _ in range(4)] for _ in range(5)]
    segments = get_booleans(digit)

    if segments[0]:
        for col in range(4):
            display[0][col] = '#'

    if segments[6]:
        for col in range(4):
            display[2][col] = '#'

    if segments[3]:
        for col in range(4):
            display[4][col] = '#'

    if segments[1]:
        display[1][3] = '#'

    if segments[2]:
        display[3][3] = '#'

    if segments[5]:
        display[1][0] = '#'

    if segments[4]:
        display[3][0] = '#'

    if digit == 7:
        display[4][3] = '#'

    return display


def get_booleans(digit: int) -> list:

    digit_to_segment = [
        [ True, True, True, True, True, True, False ],
        [ False, True, True, False, False, False, False ],
        [ True, True, False, True, True, False, True ],
        [ True, True, True, True, False, False, True ],
        [ False, True, True, False, False, True, True ],
        [ True, False, True, True, False, True, True ],
        [ True, False, True, True, True, True, True ],
        [ True, True, True, False, False, False, False ],
        [ True, True, True, True, True, True, True ],
        [ True, True, True, True, False, True, True ]
    ]
    return digit_to_segment[digit]


def print_display(display: list):
    for row in display:
        print(''.join(row))


def main():
    try:
        digit = int(input("Enter a digit (0-9): "))
        display = get_seven_segment_display(digit)
        print_display(display)
    except ValueError as e:
        print("Invalid input:", e)


if __name__ == "__main__":
    main()
