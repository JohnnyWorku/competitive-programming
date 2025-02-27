# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict

for _ in range(int(input())):
    rows, cols = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
        
    forward_dict = defaultdict(int)
    backward_dict = defaultdict(int)
    max_sum = 0

    for row in range(rows):
        for col in range(cols):
            diff = row - col
            forward_dict[diff] += matrix[row][col]
            _sum = row + col
            backward_dict[_sum] += matrix[row][col]
            
    for row in range(rows):
        for col in range(cols):
            diff = row - col
            _sum = row + col
            # We subtract the matrix[row][col] from total because it is in the sum twice
            total = forward_dict[diff] + backward_dict[_sum] - matrix[row][col]
            max_sum = max(max_sum, total)
    
    print(max_sum)