#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics:"""
from sys import stdin


status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '402': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
i = 0
total_size = i
"""Define a function to print the metrics"""


def print_metrics():
    """Prints the data"""
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{:s}: {:d}".format(key, value))



try:
    for line in stdin:
        # Split the line into words
        split_line = line.split()

        # Check if there are at least two words in the line
        if len(split_line) >= 2:
            # Get the status code and update the total size
            status = split_line[-2]
            total_size += int(split_line[-1])

            # Check status code is in our dict and update its count
            if status in status_codes:
                status_codes[status] += 1

        # Increment the line counter
        i += 1

        # Every 10 lines, print the metrics
        if (i % 10) == 0:
            print_metrics()

    # Print the final metrics
    print_metrics()

# Handle keyboard interruption (Ctrl+C)
except KeyboardInterrupt as e:
    print_metrics()
