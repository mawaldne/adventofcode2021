import fileinput

def convert(line):
    [x1,y1,x2,y2] = list(map(int, line.replace(" -> ", ",").split(",")))
    return [(x1,y1),(x2,y2)]

coor_ranges = list(map(convert, fileinput.input()))

coors = []

xmax = float('-inf')
ymax = float('-inf')

for coor_range in coor_ranges:
    (x1,y1),(x2,y2) = coor_range
    xmax = max(xmax, x1, x2)
    ymax = max(ymax, y1, y2)

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

vents = [[0] * (xmax + 1) for _ in range(ymax + 1)]

for x,y in coors:
    vents[y][x] += 1

print(len([val for row in vents for val in row if val > 1]))

