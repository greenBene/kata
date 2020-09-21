
key = '! ) " ( £ * % & > < @ a b c d e f g h i j k l m n o'

def decrypt(code, key=key):
    a_ascii = 97
    s = ''
    key = key.split(' ')

    for c in code:
        if c in key:
            i = key.index(c)
            s += chr(a_ascii + i)
        else:
            s += c

    return s
