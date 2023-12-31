#!/usr/bin/python3
"""
Log Parsing Script

This script reads log data line by line from standard input,
computes metrics, and prints statistics based on specified conditions.

Input format:
 <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption (CTRL + C),
it prints statistics:
- Total file size: File size: <total size>
- Number of lines by status code:
  possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500

Project Author:
- Author: Alexander Udeogaranya
- Email: Ogranya.alex@gmail.com
- GitHub Username: [Dr-dyrane](https://github.com/Dr-dyrane)
"""

import sys


# Initialize total file size
total_file_size = 0

# Initialize status counts dictionary
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


def print_statistics(status_counts, total_file_size):
    """
    Print statistics based on status code counts and total file size.

    Args:
        status_counts (dict): Dictionary with counts for each status code.
        total_file_size (int): Total file size.
    """
    # Print the total file size
    print("File size: {}".format(total_file_size))

    # Iterate through sorted status codes and print counts for each code
    for key, val in sorted(status_counts.items()):
        # Check if there are counts for the current status code
        if val != 0:
            # Print the status code and its count
            print("{}: {}".format(key, val))


# Initialize line count
line_count = 0

try:
    # Loop through each line in standard input
    for line in sys.stdin:
        # Split the line into a list of words and reverse the order
        line = line.split()[::-1]

        # Check if the reversed line has at least 3 elements
        if len(line) > 2:
            # Increment line count for each line processed
            line_count += 1

            # Extract file size and status code from the reversed line
            total_file_size += int(line[0])  # file size
            code = line[1]  # status code

            # Check if status code is valid
            if code in status_counts:
                # Increment status code count
                status_counts[code] += 1

            # Check if 10 lines have been processed
            if line_count == 10:
                # Print statistics and reset counter
                print_statistics(status_counts, total_file_size)

                # Reset line count to 0
                line_count = 0

finally:
    # Print final statistics before exiting
    print_statistics(status_counts, total_file_size)
