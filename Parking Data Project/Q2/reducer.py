#!/usr/bin/env python3
import sys
from collections import defaultdict

year_make_counts = defaultdict(int)

# Input comes from standard input (stdin)
for line in sys.stdin:
    year_make, count = line.strip().split('\t')
    count = int(count)
    year_make_counts[year_make] += count

# Sort the year-make counts by count in descending order and get the first item
most_common_year_make, max_count = sorted(year_make_counts.items(), key=lambda x: x[1], reverse=True)[0]

# Output the most common year-make combination and its count
print(f'{most_common_year_make}\t{max_count}')
