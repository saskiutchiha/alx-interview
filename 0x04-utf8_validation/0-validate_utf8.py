#!/usr/bin/python3
"""UTF-8 validation module.
"""

def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    """
    for number in data :
        if len(bin(number)[2:]) >= 8:
           return  False
    return True
