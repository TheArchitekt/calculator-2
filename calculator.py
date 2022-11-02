"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
while True:
    input_string = input('Enter your equation: ')
    tokens = input_string.split(' ')
