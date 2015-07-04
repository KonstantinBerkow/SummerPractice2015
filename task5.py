import sys, math

def myfunc(y):
	if y >= 0.0:
		return y**5*math.exp(-y)
	else:
		return 0.0

try:
	outfilename = sys.argv [1]
except:
	print "Usage: ", sys.argv[0], " outfile pairs "
	sys.exit(1)

ofile = open(outfilename, 'w')

args = sys.argv[2:]
i = 0
length = len(args)
while i < length:
	x = float(args[i])
	y = float(args[i + 1])
	i += 2
	fy = myfunc(y)
	ofile.write('%g %12.5e \n' % (x, fy))

ofile.close()

