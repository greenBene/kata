def fizzbuzz(i):
    s = ''

    if i%3 == 0:
        s += 'Fizz'

    if i%5 == 0:
        s += 'Buzz'

    if len(s) == 0:
        s = str(i)

    return s



def fizzbuzz_advanced(i):
    s = ''

    if (i%3 == 0) or ('3' in str(i)):
        s += 'Fizz'

    if (i%5 == 0) or ('5' in str(i)):
        s += 'Buzz'

    if len(s) == 0:
        s = str(i)

    return s
