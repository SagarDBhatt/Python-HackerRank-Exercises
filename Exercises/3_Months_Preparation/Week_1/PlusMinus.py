"""
Given the list of numbers, find the propotion of +Ve, -ve and 0 numbers.

SI:
6
-4 3 -9 0 4 1

SO:
0.500000
0.333333
0.166667
"""
from itertools import count, product


def plusMinus(arr):
    countOfPos = len(list(filter(lambda a:a>0, arr)))
    countOfNeg = len(list(filter(lambda a:a<0, arr)))
    countOfZero = len(arr) - (countOfPos + countOfNeg)

    print(f"{countOfPos/len(arr):.6f}")
    print(f"{countOfNeg/len(arr):.6f}")
    print(f"{countOfZero/len(arr):.6f}")

if __name__ == '__main__':
    print(f'Inside the main')
    try:
        n = int(input().strip())
        arr = list(map(lambda a:int(a), input().split(" ")))
        plusMinus(arr)
    except ValueError as e:
        print(f'Value Error = {e}')


