def from_roman_to_arabian_nums(roman_number: str) -> int:
    """Переводит римские цифры в арабские."""
    NUMS_TABLE = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                  (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                  (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
    roman_number = roman_number.upper()
    arabian_number = 0
    for arab, roman in NUMS_TABLE:
        while roman_number.startswith(roman):
            arabian_number += arab
            roman_number = roman_number[len(roman):]
    return arabian_number


if __name__ == "__main__":
    print(from_roman_to_arabian_nums(input('Введите римские цифры: ')))
    
