#!/bin/python3

# import math
# import os
# import random
# import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
def unboundedKnapsack(target_sum, elements):
    dp = [0] * (target_sum + 1)
    
    for value in elements:
        for j in range(value, target_sum + 1):
            dp[j] = max(dp[j], dp[j - value] + value)
    
    return dp[target_sum]

def main():
    input = sys.stdin.read
    data = input().splitlines()

    num_cases = int(data[0])
    line_index = 1
    results = []

    for _ in range(num_cases):
        n, k = map(int, data[line_index].split())
        arr = list(map(int, data[line_index + 1].split()))
        result = unboundedKnapsack(k, arr)
        results.append(result)
        line_index += 2

    for result in results:
        print(result)

if __name__ == '__main__':
    main()

