# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
lst = list(map(int, input().split()))

nums_dict = {}

for index, num in enumerate(lst):
    nums_dict[num] = index

[*indices] = nums_dict.values()
indices.sort()

for key, value in nums_dict.items():
    lst[key - 1] = value + 1

print(" ".join(map(str, lst)))