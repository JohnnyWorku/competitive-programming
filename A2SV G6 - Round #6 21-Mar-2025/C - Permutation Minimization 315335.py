# Problem: C - Permutation Minimization - https://codeforces.com/gym/594077/problem/C

from collections import deque

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    queue = deque()
    for num in nums:
        if queue and num < queue[0]:
            queue.appendleft(num)
        else:
            queue.append(num)
            
    print(*queue)