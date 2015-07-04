import sys

try:
	input_filename = sys.argv[1]
	output_filename = sys.argv[2]
except:
	print "Usage: ", sys.argv[0], " <input_file> <output_file>"
	sys.exit(1)

with open(input_filename, 'r') as inputFile:
	with open(output_filename, 'w') as outputFile:
		for line in inputFile:
			lineArgs = line.split()
			s = 0
			i = 0
			length = len(lineArgs)			
			while (i < length):
				outputFile.write(lineArgs[i] + ' ')
				s += float(lineArgs[i])
				i += 1
			outputFile.write('%12.6e\n' % (s / length))
