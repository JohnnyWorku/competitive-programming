# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    count = 0
    left = 0
    right = 1
    while left < right < n:
        if nums[left] > nums[right]:
            count += 1
            right += 2
            left += 2
        else:
            right += 1
            left += 1
            
    print(count)