#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    fun = sys.argv
    n = len(fun)
    if n == 1:
        print("{} arguments.".format(n - 1))
    elif n == 2:
        print("{} argument:".format(n - 1))
        print("{}: {}".format(n - 1, fun[1]))
    else:
        print("{} arguments:".format(n - 1))
        for i in range(1, n):
            print("{}: {}".format(i, fun[i]))
