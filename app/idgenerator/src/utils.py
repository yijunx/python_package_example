def digits_of(number_sequence: str) -> list[int]:
    return [int(digit) for digit in number_sequence]


def luhn_checksum(card_number: str) -> int:
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10