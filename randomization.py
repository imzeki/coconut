import time
import string


def randnumber(minimum: int, maximum: int) -> int:
    """
    Generates a random number
    """
    try:
        now = str(time.clock())
        rnd = float(now[::-1][:3:]) / 1000
        return int(minimum + rnd * (maximum - minimum))
    except:
        raise TypeError(f"Type given is invalid")


def choice(arg: list):
    """
    Returns a random choice from a list
    """
    if type(arg) != list:
        arg = str(arg)
        arg = [c for c in arg]
    return arg[randnumber(0, len(arg) - 1)]


def choices(arg: list, n: int):
    """
    Gets the amount of objects from the list randomly
    """
    chosen = []
    if type(n) != int:
        raise TypeError("N is not an integer")
    elif n == 1:
        return choice(arg)
    else:
        while n != 0:
            chosen.append(choice(arg))
    return chosen


def randnumberbelowmax(minimum: int, maximum: int) -> int:
    """
    Randnumber except you cannot get x
    """
    try:
        randnumber(minimum, maximum - 1)
    except:
        raise TypeError("Type given is invalid")


def randdecimal(minimum: float, maximum: float):
    """
    Returns a random decimal
    """
    if type(minimum) != float:
        raise TypeError(f"Type {minimum} cannot be used for minimum")
    elif type(maximum) != float:
        raise TypeError(f"Type {maximum} cannot be used for maximum")
    else:
        return randnumber(int(minimum), int(maximum)) / randnumber(int(minimum), int(maximum)) * 1.32


def randstr(size: int = 10):
    """
    Returns a random string. If a float is given in size, it will still accept it
    """
    if type(size) not in [int, float]:
        raise TypeError(f"Type {type(size)} is not supportable for randstr")
    else:
        C = []
        for i in range(int(size)):
            C.append(choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase +
                            string.hexdigits + string.octdigits + string.whitespace))
        return "".join(C)


def randbool():
    """
    Returns a random boolean
    """
    return choice([True, False, None])
