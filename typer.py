"""
Types is a module in Coconut to help simplify common types like str, int, float and list.(Those are the current ones)
"""
import sys
from typing import List, List
import re
import string
from collections import OrderedDict

class _String():
    """
    String is a possibly more helpful version of str. Unfortunately, it cannot support map, format, format_map, translate. istitle, title will not be in here because capitalize is improved here.
    >>> from Coconut.types import String
    >>> A = String("#")
    >>> print(A.join(["A", "B", "C", "D", "E"]))
    'A#B#C#D#E'
    >>> A = String("ABCDEFGhijklmno")
    '8:7'
    >>> A = A.extremesplit()
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'h', 'i', 'j', 'k', 'l', 'm', 'n' 'o']
    """
    def __init__(self, Object:str):
        self.Object = str(Object)
        self.uniqueFunctionsNotInStr = ["extremesplit", "gensplit", "trim", "UpperLowerCount", "find_all", "flipside", "unique", "isUnique", "length"]
        self.length = len(self.Object)

    def gensplit(self, sep=None):
        """
        Splits the string into a generator
        """
        exp = re.compile(r'\s+' if sep is None else re.escape(sep))
        position = 0
        while True:
            S = exp.search(self.Object, position)
            if not S:
                if position < len(S) or sep is not None:
                    yield self.Object[position:]
                break
            if position < S.start() or sep is not None:
                yield self.Object[position:S.start()]
            position = S.end()

    def extremesplit(self):
        """
        Splits the entire string
        >>> A = String("Eggs")
        >>> A.extremesplit()
        ['E', 'g', 'g', 's']
        >>> print(A)
        'Eggs'
        """
        return [c for c in self.Object]

    def split(self, sep:str=""):
        """
        Splits the string defined to this class.
        This is the exact same thing as list(String("Whatever object in here").gensplit())
        >>> a = String("b").split()
        ['b']
        >>> a = String("b").gensplit() #This will return a generator object
        """
        return list(self.gensplit(sep))

    def trim(self):
        """
        Gets rid of all spaces in the string. The same idea of javascript trim()
        >>> Example = String("Hello World")
        >>> Example.lstrip()
        'Hello World'
        >>> Example.rstrip()
        'Hello World'
        >>> Example.trim()
        'HelloWorld'
        """
        return ''.join([c for c in self.Object if c != " "])

    def UpperLowerCount(self):
        """
        Counts the upper and lower characters inside the string. Displays it like this: 3:1(3 is the lower and 1 is the upper)
        >>> from coconut.types import String
        >>> String("AbCdEFghIj").UpperLowerCount()
        '5:5'
        """
        upper, lower = 0, 0
        for i in range(len(self.Object)):
            if (ord(self.Object[i]) >= 97 and ord(self.Object[i]) <= 122):
                lower += 1
            elif (ord(self.Object[i]) >= 65 and ord(self.Object[i]) <= 90):
                upper += 1
            else:
                pass
        return ":".join([str(lower), str(upper)])

    def join(self, __iterable: List[str]) -> str:
        """
        Joins a list together with a string, every element in the list will be sperated by the string defined in this class
        >>> from coconut.types import String
        >>> A = String("#")
        >>> print(A.join(["A", "B", "C"]))
        'A#B#C'
        """
        returning = ""
        for i in __iterable:
            if i != __iterable[:-1]:
                returning = returning + i + self.Object
        return returning[0:len(returning)-1]

    def find_all(self, occurances:str, casesensative:bool=True) -> List[int]:
        """
        Returns all the index of the occurances of a string
        >>> A = String("A Simple String can Help Do Something")
        >>> A.find_all("a")
        [14]
        """
        occurances = str(occurances)
        if casesensative:
            return [i.start() for i in re.finditer(occurances, self.Object)]
        else:
            return [i.start() for i in re.finditer(occurances.lower(), self.Object.lower())]

    def rfind(self, occurances:str, casesensative:bool = True) -> int:
        """
        Returns the index of the last occurance in the string
        >>> from coconut.types import String
        >>> A = String("###")
        >>> print(A.rfind("#"))
        2
        """
        return max(self.find_all(occurances, casesensative))

    def isspace(self):
        """
        Checks if the string is all whitespaces
        """
        return len([o for o in self.Object if o == " "]) == self.length

    def isprintable(self):
        """
        Returns if the string is printable
        """
        return set(self.Object).issubset(set(string.printable))

    def flipside(self):
        """
        Returns a string flipped sideways
        """
        return "".join(reversed(self.Object))

    def isnumeric(self):
        """
        Returns a bool if the string can be converted to an integer
        """
        return len([n for n in self.Object if n in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']]) == self.length

    def isdecimal(self):
        """
        Ckecks if the number is a float/decimal
        """
        decimalpoints = 0
        numbers = []
        for o in self.Object:
            if o == ".":
                decimalpoints +=1
            else:
                if o in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                    numbers.append(o)
                else:
                    return False
        if decimalpoints == 1:
            if len(numbers)+1 == self.length:
                return True
            else:
                return False
        else:
            return False

    def isidentifier(self):
        """
        Checks if the string is a valid identifier
        """
        if " " in self.Object:
            return False
        else:
            if self.Object[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                return False
            else:
                for s in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-" "=", "{", "}", "[", "]", "|", "\\", ";", ":", "'", '"', "/", ">", ".", ",", "<", "~" "`"]:
                    if s in self.Object:
                        return False
                return True

    def unique(self):
        """
        Converts the string into only unique characters
        >>> from coconut.types import String
        >>> A = String("ABABABACDAYE")
        >>> B = A.unique()
        >>> print(B)
        'ABCDYE'
        """
        return ''.join(OrderedDict.fromkeys(self.Object).keys())

    def isUnique(self):
        """
        Checks if the string is only unique characters
        """
        char_set = [False] * 128
        for i in range(0, len(self.Object)):
            val = ord(self.Object[i])
            if char_set[val]:
                return False
            char_set[val] = True
        return True

    def length(self):
        """
        Returns the length of this string
        """
        return self.length

    def fill(self, filler:str):
        """
        Fills the string with the filler
        """
        return filler * self.length()

    def capitalize(self):
        """
        Returns a capitalized version of this string
        """
        final = []
        try:
            o = self.Object.split(" ")
            if len(o) == 1:
                return "".join(self.Object[0].upper() + self.Object[1:self.length].lower())
            else:
                for s in o:
                    final.append(s[0].upper() + s[1:len(s)].lower())
                return " ".join(final)
        except:
            return self.Object[0].upper() + self.Object[1:self.length()-1].lower()

    def __str__(self):
        return self.Object

class _Integer:
    """
    """

class _Float:
    """
    """

class _List:
    """
    """

class _Percentage:
    """
    """

String = _String
Integer = _Integer
Float = _Float
List = _List
Percentage = _Percentage

print(String("okay boomer?").capitalize())