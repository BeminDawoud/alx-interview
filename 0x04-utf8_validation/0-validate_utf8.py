#!/usr/bin/python3
"""
UTF-8 Validation.
"""


def validUTF8(data):
    """Check if data is a valid UTF-8 encoding."""
    num_bytes = 0
    mask1 = 0b10000000
    mask2 = 0b11000000

    for num in data:
        if num_bytes == 0:
            if (num & mask1) == 0:
                continue
            elif (num & 0b11100000) == 0b11000000:
                num_bytes = 1
                if num < 0b11000010:
                    return False
            elif (num & 0b11110000) == 0b11100000:
                num_bytes = 2
                if num == 0b11100000 and (data[1] & mask1) == 0:
                    return False
                if num == 0b11101101 and (data[1] & 0b11100000) == 0b10100000:
                    return False
            elif (num & 0b11111000) == 0b11110000:
                num_bytes = 3
                if num == 0b11110000 and (data[1] & 0b11110000) == 0:
                    return False
                if num > 0b11110100:
                    return False
            else:
                return False
        else:
            if (num & mask2) != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0
