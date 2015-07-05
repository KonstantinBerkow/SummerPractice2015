import sys, math, random

n = int(sys.argv[1])
count = 0
for i in range(0, n):
	x = random.randint(1, 6)
	y = random.randint(1, 6)
	if (x == 6 or y == 6):
		count += 1

print float(count) / n
