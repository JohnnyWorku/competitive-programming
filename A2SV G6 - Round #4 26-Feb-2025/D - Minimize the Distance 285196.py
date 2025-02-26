# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
points = list(map(int, input().split()))

points.sort()

if n != 1:
    i = (n + 1) // 2
    print(points[i - 1])
else:
    i = n // 2
    print(points[i - 1])