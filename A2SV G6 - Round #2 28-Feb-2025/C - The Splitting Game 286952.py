# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter, defaultdict

for _ in range(int(input())):
    s_length = int(input())
    s = input()
    
    right_side_counter = Counter(s)
    left_side_counter = defaultdict(int)
    max_length = 0
    
    for i in range(s_length):
        left_side_counter[s[i]] += 1
        right_side_counter[s[i]] -= 1
        if right_side_counter[s[i]] == 0:
            del right_side_counter[s[i]]
            
        their_length_sum = len(left_side_counter) + len(right_side_counter)
        max_length = max(max_length, their_length_sum)
        
    print(max_length)