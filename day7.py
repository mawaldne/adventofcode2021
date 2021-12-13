import fileinput
from collections import defaultdict

line = fileinput.input().readline()
crab_positions = list(map(int, line.split(",")))

def summation(n):
    return (n*(n + 1))/2

max_pos = max(crab_positions)
min_pos = min(crab_positions)

least_fuel = float("inf")
for pos in range(min_pos, max_pos):
    fuel = sum([abs(crab_pos - pos) for crab_pos in crab_positions])
    least_fuel = fuel if fuel < least_fuel else least_fuel

print(least_fuel)

least_fuel = float("inf")
for pos in range(min_pos, max_pos):
    fuel = sum([summation(abs(crab_pos - pos)) for crab_pos in crab_positions])
    #print(f"pos: {pos}, fuel: {fuel}")
    least_fuel = fuel if fuel < least_fuel else least_fuel

print(least_fuel)


