#!/usr/bin/env python3
import sys
import json

def extract_hour(violation_time):
    # Directly extract the hour part (first two characters)
    hour_part = violation_time[:2]
    # Convert the hour part to an integer
    try:
        hour = int(hour_part)
    except ValueError:
        return None  # Return None for invalid hour

    # Adjust the hour based on the AM/PM indicator
    if violation_time[-1] == 'P' and hour < 12:
        hour += 12
    elif violation_time[-1] == 'A' and hour == 12:
        # Special case for midnight
        hour = 0
    return hour

# Input comes from standard input (stdin)
for line in sys.stdin:
    cleaned_line = line.lstrip(',')
    try:
        record = json.loads(cleaned_line)
        violation_time = record.get('violation_time', '')
        hour = extract_hour(violation_time)

        if hour is not None:
            # Output the key-value pair with hour as the key and 1 as the value
            print(f'{hour}\t1')
    except ValueError:
        continue
