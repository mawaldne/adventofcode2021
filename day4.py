import fileinput

drawn = []
for line in fileinput.input():
    if fileinput.isfirstline():
        drawn = line.strip.split(",")

print(drawn)

