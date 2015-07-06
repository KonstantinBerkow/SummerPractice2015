import sys, random

tryCount = int(sys.argv[1])
succes = 0
for i in range(0, tryCount):
	s = random.randint(1, 6)
	s += random.randint(1, 6)
	s += random.randint(1, 6)
	s += random.randint(1, 6)
	if s < 9:
		succes += 1

print 'Probability of succesfull rolls: %.3f' % (float(succes) / tryCount)
print 'Balance after such game: %d' % (succes * 10 - tryCount)
