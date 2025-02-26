# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

nums = [num for num in range(1, 1001)]

nums_string = "".join(map(str, nums))

index = int(input()) - 1
print(nums_string[index])