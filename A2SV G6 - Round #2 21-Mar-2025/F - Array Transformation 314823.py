# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    nums_counter = defaultdict(int)
    freq_counter = defaultdict(int)
    
    for num in nums:
        nums_counter[num] += 1
        freq_counter[nums_counter[num]] += 1
    
    min_removes = float("inf")
    for key, val in freq_counter.items():
        curr_remove = n - (key * val)
        min_removes = min(curr_remove, min_removes)
        
    print(min_removes)