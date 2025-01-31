#!/usr/bin/env python3
import sys
from collections import defaultdict

county_counts = defaultdict(int)

# Input comes from standard input (stdin)
for line in sys.stdin:
    county, count = line.strip().split('\t')
    count = int(count)
    county_counts[county] += count

# Sort the county counts by count in descending order and get the first item
most_common_counties = sorted(county_counts.items(), key=lambda x: x[1], reverse=True)[:1]

# Output the top 3 most common counties and their counts
for county, count in most_common_counties:
    print(f'{county}\t{count}')

