#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    cleaned_line = line.lstrip(',')
    try:
        record = json.loads(cleaned_line)
        vehicle_color = record.get('vehicle_color', '').strip().upper()  # Normalize color to uppercase

        if vehicle_color:
            print(f'{vehicle_color}\t1')
    except ValueError:
        continue
