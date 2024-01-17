from learn_testing.area.exception_zero import NegativeError
import math


def rectangle(a :int, b :int) ->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    elif a < 0 or b < 0:
        raise NegativeError
    else:
        return a * b


def triangle(a :int, b :int)->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0 or b < 0:
        raise NegativeError
    else:
        return a * b / 2


def hexagon(a :int)->float:
    if not isinstance(a, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0:
        raise NegativeError
    else:
        return (3 * math.sqrt(3) / 2) * pow(a, 2)


def circle(a :int)->float:
    if not isinstance(a, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0:
        raise NegativeError
    else:
        return math.pi * pow(a, 2)
