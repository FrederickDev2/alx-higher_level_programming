<<<<<<< HEAD
#!/usr/bin/python3
""" Write a program that imports all functions from
the file calculator_1.py and handles basic operations.
"""
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == "+":
        sum = add(int(sys.argv[1]), int(sys.argv[3]))
        print(
            "{} {} {} = {}".format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sum))
    elif sys.argv[2] == "-":
        sub_ = sub(int(sys.argv[1]), int(sys.argv[3]))
        print(
            "{} {} {} = {}".format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sub_))
    elif sys.argv[2] == "*":
        mul_ = mul(int(sys.argv[1]), int(sys.argv[3]))
        print(
            "{} {} {} = {}".format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                mul_))
    elif sys.argv[2] == "/":
        div_ = div(int(sys.argv[1]), int(sys.argv[3]))
        print(
            "{} {} {} = {}".format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                div_))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
=======
#!/usr/bin/python3


if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == '+':
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif sys.argv[2] == '-':
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif sys.argv[2] == '*':
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    else:
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
>>>>>>> c2505d1cad6bf7a56dbe6b724df65584286d18a6
