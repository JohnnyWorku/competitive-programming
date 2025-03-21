# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

if sum(a) != sum(b):
    print("-1")
    exit()

a_runner, b_runner = 0, 0
a_pointer, b_pointer = 0, 0
counter = 0

while a_pointer < n:
    a_runner += a[a_pointer]
    a_pointer += 1
    b_runner += b[b_pointer]
    b_pointer += 1
    
    while a_runner != b_runner:
        if a_runner <= b_runner:
            a_runner += a[a_pointer]
            a_pointer += 1
        else:
            b_runner += b[b_pointer]
            b_pointer += 1
            
    counter += 1
    
print(counter)
