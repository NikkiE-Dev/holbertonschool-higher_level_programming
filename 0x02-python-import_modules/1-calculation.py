#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    total1 = add(a, b)
    total2 = sub(a, b)
    total3 = mul(a, b)
    total4 = div(a, b)
    print("{} + {} = {}".format(a, b, total1))
    print("{} - {} = {}".format(a, b, total2))
    print("{} * {} = {}".format(a, b, total3))
    print("{} / {} = {}".format(a, b, total4))
