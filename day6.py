import fileinput
from collections import defaultdict

lanternfish = list(map(int, fileinput.input()[0].split(",")))

fishtimerhash = defaultdict(int)

for f in lanternfish:
    fishtimerhash[f] += 1

print(fishtimerhash)

for _ in range(256):
    newtimerhash = defaultdict(int)
    newtimerhash[8] = fishtimerhash[0]
    newtimerhash[6] = fishtimerhash[0]

    if 0 in fishtimerhash:
        del fishtimerhash[0]

    for time, totalfish in fishtimerhash.items():
        newtimerhash[time - 1] += totalfish

    fishtimerhash = newtimerhash
    # print(fishtimerhash)

print(sum(fishtimerhash.values()))


