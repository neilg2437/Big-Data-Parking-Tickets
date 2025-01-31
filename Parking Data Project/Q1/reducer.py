#!/usr/bin/env python3
import sys
from collections import defaultdict

hourly_counts = defaultdict(int)

# Input comes from standard input (stdin)
for line in sys.stdin:
    hour, count = line.strip().split('\t')
    count = int(count)
    hourly_counts[hour] += count

# Sort the hourly counts by count in ascending order and get the last item
max_hour, max_count = sorted(hourly_counts.items(), key=lambda x: x[1])[-1]

# Output the hour with the highest total count and its count
print(f'{max_hour}\t{max_count}')
