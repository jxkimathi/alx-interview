#!/usr/bin/python3

"""Import necessary modules"""

import sys

"""Define a function to print total file size and status codes"""


def _print(total_file_size, statuses):
    """Prints the total file size and counts of each status code."""
    print("File size: {:d}".format(total_file_size))
    for key, value in sorted(statuses.items()):
        if value != 0:
            print("{}: {}".format(key, value))


# Initialize a dictionary to count occurrences of specific status codes
statuses = {
    '200': 0, '301': 0,
    '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0
}

total_file_size = 0
count = 0

try:
    # Read each line from standard input
    for line in sys.stdin:
        args = line.split()

        # Ensure the line has enough elements to extract status code
        if len(args) > 2:
            status_code = args[-2]
            file_size = int(args[-1])

            # Update the status code count
            if status_code in statuses:
                statuses[status_code] += 1

            # Update the total file size
            total_file_size += file_size
            count += 1

            # Print stats every 10 lines
            if count == 10:
                _print(total_file_size, statuses)
                count = 0

except KeyboardInterrupt:
    pass

finally:
    # Print final stats when the process ends
    _print(total_file_size, statuses)
