import fileinput
from collections import defaultdict

def convert(line):
    return list(map(int, line.replace(" -> ", ",").split(",")))

coor_ranges = list(map(convert, fileinput.input()))
coors = []

for x1,y1,x2,y2 in coor_ranges:
    if y1 == y2:
        if x1 < x2:
            c = [(x,y1) for x in range(x1,x2 + 1)]
        else:
            c = [(x,y1) for x in range(x1,x2 - 1,-1)]
    elif x1 == x2:
        if y1 < y2:
            c = [(x1,y) for y in range(y1,y2 + 1)]
        else:
            c = [(x1,y) for y in range(y1,y2 - 1,-1)]

    coors += c
    c = []


vents = defaultdict(int)
for coor in coors:
    vents[coor] += 1
print(len([val for val in vents.values() if val > 1]))

