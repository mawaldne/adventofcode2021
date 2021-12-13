nums = []

with open('day1.txt', 'r') as l:
    lines = l.readlines()
    for line in lines:
        nums.append(int(line.strip()))

prev = nums[0]
increases = 0

for i in range(1, len(nums)):
    num = nums[i]

    if num > prev:
        increases += 1

    prev = num

print(increases)
