import math


def sum(a :int, b :int)->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    else:
        return a + b


def subs(a :int, b :int)->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    else:
        return a - b


def mult(a :int, b :int)->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    else:
        return a * b


def div(a :int, b :int)->float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    elif b == 0:
        raise ZeroDivisionError("Divisor 0 in ", __name__)
    else:
        return a / b


def power(a :int, b :int)->int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("not integer passed in ", __name__)
    else:
        return pow(a, b)


def sqrot(a :int)->float:
    if not isinstance(a, int):
        raise TypeError("not integer passed in ", __name__)
    elif a < 0:
        raise ValueError("Out of domain in ", __name__)
    else:
        return math.sqrt(a)
