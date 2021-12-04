# Day 2: Run as:
#
# python day2.py day2.txt
#

from typing import Tuple
import fileinput

def convert(line: str) -> tuple[str, int]:
    vals = line.split()
    return (vals[0], int(vals[1]))

values = list(map(convert, fileinput.input()))

x,y = 0,0
for direction, val in values:
    if direction == 'forward':
        x += val
    elif direction == 'down':
        y += val
    elif direction == 'up':
        y -= val
    else:
        print("Something strange here...")

print(x,y)
print(x*y)

x,y = 0,0
aim = 0
for direction, val in values:
    if direction == 'forward':
        x += val
        y += aim * val
    elif direction == 'down':
        aim += val
    elif direction == 'up':
        aim -= val
    else:
        print("Something strange here...")

print(x,y)
print(x*y)
