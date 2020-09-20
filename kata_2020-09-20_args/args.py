import sys
from enum import Enum

class DataType(Enum):
    bool = 1
    string = 2
    int = 3
    list = 4

class InvalidParameterException(Exception):
    pass


schema = [
 ('-b', DataType.bool, False),
 ('-s', DataType.string, ''),
 ('-i', DataType.int, 0),
 ('-l', DataType.list, [])
]


def arguments_parsing(argv, schema=schema):
    ''' Parses given parameters, based on schema

    Args:
    - argv (list[string]):
    - schema (list[(flag, type, default_value)])

    Returns
    - list[(flag, value)]: Parsed arguments

    '''
    parsed_arguments = []

    for arg in schema:
        flag, type, default = arg[0], arg[1], arg[2]
        value = None

        if type == DataType.bool:
            value = parse_bool(flag, default, argv)

        elif type == DataType.string:
            value = parse_string(flag, default, argv)

        elif type == DataType.int:
            value = parse_int(flag, default, argv)

        elif type == DataType.list:
            value = parse_list(flag, default, argv)

        parsed_arguments += [(flag, value)]

    return parsed_arguments


def parse_bool(flag, default, argv):
    if flag not in argv:
        return default
    else:
        return True


def parse_string(flag, default, argv):
    if flag not in argv:
        return default

    try:
        i = argv.index(flag)
        value = argv[i+1]
        return value

    except IndexError:
        raise InvalidParameterException('Missing string value after flag {}.'.format(flag))


def parse_int(flag, default, argv):
    if flag not in argv:
        return default

    try:
        i = argv.index(flag)
        value = argv[i+1]
        value = int(value)
        return value

    except IndexError:
        raise InvalidParameterException('Missing integer value after flag {}.'.format(flag))
    except ValueError:
        raise InvalidParameterException('Invalid integer value ({}) after flag {}.'.format(value, flag))

def parse_list(flag, default, argv):
    if flag not in argv:
        return default

    try:
        i = argv.index(flag)
        list = argv[i+1]
        list = list.split(',')
        return list
    except IndexError:
        raise InvalidParameterException('Missing list value after flag {}.'.format(flag))




if __name__ == '__main__':
    print(arguments_parsing(sys.argv))
