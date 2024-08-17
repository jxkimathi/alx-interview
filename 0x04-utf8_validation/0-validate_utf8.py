#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """Determines if a given data set represents valid UTF-8 encoding"""
    num_bytes = 0
    for num in data:
        bin_rep = format(num, '#010b')[-8:]

        if num_bytes == 0:
            if bin_rep[0] == '0':
                continue
            elif bin_rep[:3] == '110':
                num_bytes = 1
            elif bin_rep[:4] == '1110':
                num_bytes = 2
            elif bin_rep[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            if bin_rep[:2] != '10':
                return False
            num_bytes -= 1

    return num_bytes == 0
