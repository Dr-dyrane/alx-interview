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


def print_statistics(status_counts, total_file_size):
    """
    Print statistics based on status code counts and total file size.

    Args:
        status_counts (dict): Dictionary with counts for each status code.
        total_file_size (int): Total file size.
    """
    # Print the total file size
    print(f"File size: {total_file_size}")

    # Iterate through sorted status codes and print counts for each code
    for code in sorted(status_counts):
        count = status_counts[code]

        # Check if there are counts for the current status code
        if count > 0:
            # Print the status code and its count
            print(f"{code}: {count}")


def main():
    """
    Read log data from standard input, compute metrics, and print statistics.
    """
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

    # Initialize line count
    line_count = 0

    try:
        # Loop through each line in standard input
        for line in sys.stdin:
            # Increment line count for each line processed
            line_count += 1

            # Check if 10 lines have been processed
            if line_count > 10:
                # Reset line count to 1
                line_count = 1

                # Print statistics and reset counters
                print_statistics(status_counts, total_file_size)

                # Reset total file size to 0
                total_file_size = 0
                # Reset status_counts using a dictionary comprehension
                status_counts = {key: 0 for key in status_counts}

            # Split the line into parts
            parts = line.split()

            # Check conditions for valid log entry and update metrics
            if (len(parts) >= 8 and
                    parts[-3].isdigit() and
                    parts[-2] in status_counts):
                # Update total file size and increment status code count
                total_file_size += int(parts[-3])
                status_counts[parts[-2]] += 1

    except KeyboardInterrupt:
        pass  # Allow graceful exit on Ctrl+C

    finally:
        # Print final statistics before exiting
        print_statistics(status_counts, total_file_size)


if __name__ == "__main__":
    # If this script is run as the main module, execute the main() function
    main()
