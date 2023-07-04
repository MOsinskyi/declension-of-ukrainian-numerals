from dictionary import *


def declension_number(number):
    if number == 0:
        return 'нуль'

    def convert_to_words(n, case):
        words = CASES[case]
        if n < 10:
            return words[0][n]
        elif n < 20:
            return words[1][n - 10]
        elif n < 100:
            return words[2][n // 10] + ' ' + words[0][n % 10]
        elif n < 1000 and case in [0, 1, 2, 3, 4, 5]:
            return words[3][n // 100] + ' ' + convert_to_words(n % 100, case)
        elif n < 10000 and case in [0, 1, 2, 3, 4, 5]:
            if n // 1000 != 1:
                return words[0][n // 1000] + ' ' + THOUSANDS[case][n // 1000] + ' ' + convert_to_words(n % 1000, case)
            else:
                return THOUSANDS[case][n // 1000] + ' ' + convert_to_words(n % 1000, case)
        elif n < 20000 and case in [0, 1, 2, 3, 4, 5]:
            return words[1][n // 10000] + ' ' + THOUSANDS[case][n // 10000] + ' ' + convert_to_words(n % 10000, case)
        elif n < 100000 and case in [0, 1, 2, 3, 4, 5]:
            return words[2][n // 10000] + ' ' + convert_to_words(n % 10000, case)
        elif n < 1000000 and case in [0, 1, 2, 3, 4, 5]:
            return words[3][n // 100000] + ' ' + convert_to_words(n % 100000, case)

    nominative_number = convert_to_words(number, 0)
    genitive_number = convert_to_words(number, 1)
    dative_number = convert_to_words(number, 2)
    accusative_number = convert_to_words(number, 3)
    ablative_number = convert_to_words(number, 4)
    local_number = convert_to_words(number, 5)

    return nominative_number, genitive_number, dative_number, accusative_number, ablative_number, local_number
