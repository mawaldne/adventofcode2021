import fileinput

BINARY_SIZE = 12

def convert(line: str) -> str:
    return line.strip()

def position_counts(values, size):
    pc = [[0,0] for _ in range(size)]

    for val in values:
        for i in range(len(val)):
            if val[i] == '0':
                pc[i][0] += 1
            else:
                pc[i][1] += 1
    return pc


binary_values = list(map(convert, fileinput.input()))
gamma = int("".join(['0' if a > b else '1' for a,b in position_counts(binary_values, BINARY_SIZE)]),2)
delta = gamma ^ int("1" * BINARY_SIZE, 2)

print(gamma, delta)
print(gamma * delta)


o2_values = binary_values.copy()
for i in range(BINARY_SIZE):
    pc = position_counts(o2_values, BINARY_SIZE)
    o2_bit = "0" if pc[i][0] > pc[i][1] else "1"
    next_o2_values = []

    for o2_value in o2_values:
        if o2_value[i] == o2_bit:
            next_o2_values.append(o2_value)
    o2_values = next_o2_values.copy()

    if len(o2_values) == 1:
        break
print(o2_values[0])

co2_values = binary_values.copy()
for i in range(BINARY_SIZE):
    pc = position_counts(co2_values, BINARY_SIZE)
    co2_bit = "0" if pc[i][0] <= pc[i][1] else "1"
    next_co2_values = []

    for co2_value in co2_values:
        if co2_value[i] == co2_bit:
            next_co2_values.append(co2_value)
    co2_values = next_co2_values.copy()

    if len(co2_values) == 1:
        break
print(co2_values[0])

print(int(o2_values[0],2) * int(co2_values[0],2))
