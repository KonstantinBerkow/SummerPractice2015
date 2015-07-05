import math, random

n = 0
count = 0
prob = 2.0 / 6
empProb = 0
while True:
	n += 1
	x = random.randint(1, 6)
	y = random.randint(1, 6)
	if (x == 6 or y == 6):
		count += 1
	empProb = float(count) / n
	if math.fabs(empProb - prob) < 1e-3:
		break

print 'try count: %d' % n

