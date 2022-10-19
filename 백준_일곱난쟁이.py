from itertools import combinations
import sys

input=sys.stdin.readline
height=[ int(input()) for i in range(9)]
for h in combinations(height,7):
    if sum(h)<100:
        for i in sorted(h):
            print(i)
        break