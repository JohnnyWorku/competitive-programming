# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
left = 0
inc_queue = deque()
dec_queue = deque()

for right in range(len(nums)):
    while inc_queue and inc_queue[-1] > nums[right]:
        inc_queue.pop()
        
    inc_queue.append(nums[right])
    
    while dec_queue and dec_queue[-1] < nums[right]:
        dec_queue.pop()
        
    dec_queue.append(nums[right])
    
    while (inc_queue and dec_queue) and (dec_queue[0] - inc_queue[0] > k):
        if nums[left] == inc_queue[0]:
            inc_queue.popleft()
        if nums[left] == dec_queue[0]:
            dec_queue.popleft()
            
        left += 1
        
    count += right - left + 1
    
print(count)