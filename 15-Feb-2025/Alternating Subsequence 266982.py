# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

for _ in range(int(input())):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    last_no, _sum = arr[0], arr[0]
    for i in range(arr_len):
        if last_no > 0 and arr[i] > 0 or last_no < 0 and arr[i] < 0:
            if arr[i] > last_no:
                # _sum = (_sum - last_no) + arr[i]
                _sum += arr[i] - last_no
                last_no = arr[i]

        else:
            _sum += arr[i]
            last_no = arr[i]

    print(_sum)