#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing 1 byte of data each.
    :return: True if data is a valid UTF-8 encoding, else False.
    """
    # Helper function to check if a given byte is a valid UTF-8 start byte
    def is_start_byte(byte):
        return (byte & 0b10000000) == 0b00000000

    # Helper function to check if a given byte is a valid UTF-8 follow byte
    def is_follow_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    # Variable to track the expected number of following bytes
    following_bytes = 0

    # Iterate through each byte in the data
    for byte in data:
        # If no following bytes are expected
        if following_bytes == 0:
            if is_start_byte(byte):
                # Single-byte character
                continue
            elif (byte & 0b11100000) == 0b11000000:
                # Two-byte character
                following_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                # Three-byte character
                following_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                # Four-byte character
                following_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Check if the byte is a valid follow byte
            if not is_follow_byte(byte):
                return False
            following_bytes -= 1

    # If there are remaining expected following bytes, it's invalid
    return following_bytes == 0
