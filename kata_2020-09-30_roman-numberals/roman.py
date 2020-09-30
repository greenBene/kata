roman_numerals = [('I', 'V', 'X'),
                  ('X', 'L', 'C'),
                  ('C', 'D', 'M'),
                  ('M', '', '')]


def decimalToRoman(number):
    if number not in range (0, 4000):
        raise Exception('Only supports numbers between 0 and 4000')

    roman_number = ''
    for order_of_magnitude in range(0, 4):
        digit = get_digit(number, order_of_magnitude)
        romal_digit = digit_to_numeral(digit, order_of_magnitude)
        roman_number = romal_digit + roman_number

    return roman_number


def get_digit(number, order_of_magnitude):
    digit = number % (10 ** (order_of_magnitude + 1))
    digit = digit / (10 ** order_of_magnitude)
    digit = int(digit)
    return digit

def digit_to_numeral(digit, order_of_magnitude):
    one_numaral = roman_numerals[order_of_magnitude][0]
    five_numaral = roman_numerals[order_of_magnitude][1]
    ten_numeral = roman_numerals[order_of_magnitude][2]

    if digit in [0,1,2,3]:
        return digit * one_numaral
    if digit == 4:
        return one_numaral + five_numaral
    if digit in [5,6,7,8]:
        return five_numaral + (digit - 5 ) * one_numaral
    if digit == 9:
        return one_numaral + ten_numeral
