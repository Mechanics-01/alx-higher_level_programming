#!/usr/bin/python3
if __name__ == "__mnain__":
    from calculator_1 import add, sub, mul, di
    
    a = 10
    b = 5
    print('{:d} + {:d} = {:d}'.format(a, b, (add(a, b))))
    print('{:d} - {:d} = {:d}'.format(a, b, (sub(a, b))))
    print('{:d} * {:d} = {:d}'.format(a, b, (mul(a, b))))
    print('{:d} / {:d} = {:d}'.format(a, b, (div(a, b))))
