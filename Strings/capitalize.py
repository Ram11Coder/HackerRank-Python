#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    res = ''
    is_capital = True
    for i in s:
        if i.isalpha() and is_capital:
            res += i.capitalize()
            is_capital = False
        else:
            res += i
            is_capital = i == " "

    return res


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
print(result)
# fptr.write(result + '\n')

# fptr.close()
