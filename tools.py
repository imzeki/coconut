"""
Coconut has some tools to help make code shorter
>>> from coconut.tools import isExecutable
>>> isExecutable("print('Hello World!')")
True
>>> isExecutable("printt('Hello World!')") #There is a typo, it is typed as printt instead of print
False
"""


def isExecutable(code: str) -> bool:
    """
    Shows if the code is executable
    """
    try:
        exec(code)
        return True
    except:
        return False
