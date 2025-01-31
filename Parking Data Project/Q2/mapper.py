#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    cleaned_line = line.lstrip(',')
    try:
        record = json.loads(cleaned_line)
        vehicle_year = record.get('vehicle_year', '').strip()
        vehicle_type = record.get('vehicle_make', '').strip()

        # Skip records with invalid or placeholder years
        if vehicle_year.isdigit() and 1900 <= int(vehicle_year) <= 2023 and vehicle_type:
            year_make_combination = f'{vehicle_year}_{vehicle_type}'
            print(f'{year_make_combination}\t1')
    except ValueError:
        continue

