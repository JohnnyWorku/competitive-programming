# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

# Use the concept that the ord(l) < ord(m) < ord(s)
for _ in range(int(input())):
    a, b = input().split()

    if ord(a[-1]) == ord(b[-1]):
        if a[-1] == "S": # or it can be b[-1]
            if len(a) > len(b):
                print("<")
            elif len(a) > len(b):
                print(">")
            else:
                print("=")
        else:
            if len(a) > len(b):
                print(">")
            elif len(a) > len(b):
                print("<")
            else:
                print("=")

    elif ord(a[-1]) < ord(b[-1]):
        print(">")
    else:
        print("<")