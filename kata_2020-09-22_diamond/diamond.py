def diamond(letter):
    if ord(letter) < ord('A') or ord(letter) > ord('Z'):
        raise Exception('Invalid input. Only capital roman letters are a valid input.')

    position = ord(letter) - ord('A')
    ret = ''

    for i in range(position, -1, -1):
        outer_space = ' ' * (position - i)
        inner_space = ' ' * (i * 2 - 1)
        character = chr(ord('A') + i)

        if i == 0:
            new_line = outer_space + character + outer_space
        else:
            new_line = outer_space + character + inner_space + character + outer_space

        if ret == '':
            ret = new_line
        else:
            ret = new_line + '\n' + ret + '\n' + new_line

    return ret
