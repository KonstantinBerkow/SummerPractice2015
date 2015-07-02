import sys
import math

def printLog(arg):
    try:
        tmp = float(arg)
        if (tmp > 0):
            print "ln(%g) is %g" % (tmp, math.log(tmp))
        else:
            print "no ln for %g" % tmp
    except ValueError:
        print arg + " must be float!"
    return

for r in sys.argv[1:]:
        printLog(r)

for i in range(1, len(sys.argv)):
        printLog(sys.argv[i])

j = 1
while j < len(sys.argv):
    printLog(sys.argv[j])
    j += 1

k = 1
while True:
    try:
        printLog(sys.argv[k])
        k += 1
    except LookupError:
        break
