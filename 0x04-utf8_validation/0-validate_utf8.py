#!/usr/bin/python3
"""
UFT8 Validation.
"""


def validUTF8(data):
    """check if data is utf 8 valid"""
    num_bytes = 0
    mask1 = 0b10000000
    mask2 = 0b11000000

    for num in data:
        if num_bytes == 0:
            if (num & mask1) == 0:
                continue
            elif (num & mask2) == 0b11000000:
                num_bytes = 1
            elif (num & 0b11100000) == 0b11100000:
                num_bytes = 2
            elif (num & 0b11110000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if (num & mask2) != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0
