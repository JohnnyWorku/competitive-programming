# Problem: Books - https://codeforces.com/contest/279/problem/B

no_books, free_time = map(int, input().split())
books = list(map(int, input().split()))

_sum = 0
left = 0
max_books = 0

for right in range(no_books):
    _sum += books[right]
    while _sum > free_time:
        _sum -= books[left]
        left += 1

    max_books = max(max_books, right - left + 1)

print(max_books)