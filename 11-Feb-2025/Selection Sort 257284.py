# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[i] = arr[j]
            print(*arr)
            i = j
            j -= 1
        else:
            arr[j + 1] = key

    print(*arr)
                
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
