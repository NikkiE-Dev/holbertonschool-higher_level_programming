#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    a = n - 1
    num = 1

    if n == 1:
        print(a, "arguments.")

    else:
        print(a, "arguments:")
        while (a >= num):
            print ("{}: {}".format(num, sys.argv[num]))
            num = num + 1
