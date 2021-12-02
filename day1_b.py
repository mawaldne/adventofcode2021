nums = []
with open('day1.txt', 'r') as l:
    lines = l.readlines()
    for line in lines:
        nums.append(int(line.strip()))

prev = nums[0] + nums[1] + nums[2]
increases = 0

for i in range(1, len(nums) - 2):
    num = nums[i] + nums[i+1] + nums[i+2]

    if num > prev:
        increases += 1

    prev = num

print(increases)
