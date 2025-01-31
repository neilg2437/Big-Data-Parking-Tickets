#!/usr/bin/env python3
import sys
import json

# Input comes from standard input (stdin)
for line in sys.stdin:
    cleaned_line = line.lstrip(',')
    try:
        record = json.loads(cleaned_line)
        violation_county = record.get('violation_county', '').strip()

        # Ensure the county is present
        if violation_county:
            print(f'{violation_county}\t1')
    except ValueError:
        continue

