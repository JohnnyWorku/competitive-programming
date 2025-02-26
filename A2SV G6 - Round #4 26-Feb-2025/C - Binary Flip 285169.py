# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

# The idea is to be equal all sections with equal no of 0s and 1s must be same are totally opposite
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    
    counter_a = defaultdict(int)
    Failed = False
    
    left = -1
    diff = 0  # to track thier difference characters
    for right in range(n): # It can be len(b) since they are equal
        counter_a[a[right]] += 1
        if a[right] != b[right]:
            diff += 1
            
        if counter_a["0"] == counter_a["1"]:
            if diff > 0:
                if right - left == diff:
                    diff = 0 # It can be flipped
                else:
                    Failed = True
            left = right
            counter_a.clear()
            
    if diff > 0 :
        if n - left == diff:
            diff = 0
        else:
            Failed = True
                    
    if Failed:
        print("NO")
    else:
        print("YES")