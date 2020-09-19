"""
Stores math equations and formulas inside
"""


class EMC2Error(BaseException):
    """
    Error called when EMC2 gone wrong
    """
    pass


pi = 3.1415926535897932385
e = 2.7182818284590452354
sqrt2 = 1.4142135623730950488
sqrt5 = 2.2360679774997896964
phi = 1.6180339887498948482
ln2 = 0.69314718055994530942
ln10 = 2.302585092994045684
euler = 0.57721566490153286061
catalan = 0.91596559417721901505
khinchin = 2.6854520010653064453
apery = 1.2020569031595942854
logpi = 1.1447298858494001741


def mean(*l: int or float) -> int or float:
    """
    Returns the average of the numbers full of integers and floats, any other types will be discluded.
    """
    l = list(l)
    average = sum([i for i in l if type(i) in [int, float]])
    average = average / len(str(average))
    if average.is_integer():
        return int(average)
    else:
        return average


def median(*l):
    return l[min(range(len(l)), key=lambda i: abs(l[i] - mean(l)))]


def EMC2(M: int or float):
    """
    Calculates the famous equation from Einstein E = MC2
    """
    if type(M) in [int, float]:
        return M * ((3 * (10 ** 8)) ** 2)
    else:
        raise EMC2Error("E = mc2 went wrong as M is not an integer or float")
