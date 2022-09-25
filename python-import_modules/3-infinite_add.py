#!/usr/bin/python3
import sys
#nombre = sys.argv[0]
#arguments = sys.argv[1:]
#count = len(arguments)
print("{}: argument".format(len(sys.argv - 1)))
for x in sys.argv:
	print("{}".format(x))
