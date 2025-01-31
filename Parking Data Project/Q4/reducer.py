#!/usr/bin/env python3
import sys
from collections import defaultdict

color_counts = defaultdict(int)

for line in sys.stdin:
    color, count = line.strip().split('\t')
    count = int(count)
    color_counts[color] += count

# Sort the color counts by count in descending order and get the top 1
most_common_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)[:1]

for color, count in most_common_colors:
    print(f'{color}\t{count}')
