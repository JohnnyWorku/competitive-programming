# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

arr_len, k = map(int, input().split())
arr = input().split()

left = 0
nums_dict = defaultdict(int)
max_len = 0
s = 0
e = 0

for right in range(arr_len):
    nums_dict[arr[right]] += 1
    while len(nums_dict) > k:
        nums_dict[arr[left]] -= 1
        if nums_dict[arr[left]] == 0:
            del nums_dict[arr[left]]

        left += 1

    if right - left + 1 > max_len:
        s = left + 1
        e = right + 1
        max_len = right - left + 1

print(*(s, e))