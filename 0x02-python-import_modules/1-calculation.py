#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calcu

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calcu.add(a, b)))
    print("{} - {} = {}".format(a, b, calcu.sub(a, b)))
    print("{} * {} = {}".format(a, b, calcu.mul(a, b)))
    print("{} / {} = {}".format(a, b, calcu.div(a, b)))
