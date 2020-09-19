"""
Text to speech in Coconut
"""

def speak(text:str):
    """
    Speak out what is given in text
    """
    from win32com.client import Dispatch
    Dispatch("SAPI.SpVoice").speak(str(text))


