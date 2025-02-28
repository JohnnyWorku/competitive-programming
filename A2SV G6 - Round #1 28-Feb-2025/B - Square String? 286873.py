# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

for _ in range(int(input())):
    given_string = input()
    
    middle = len(given_string) // 2
    
    if given_string[:middle] == given_string[middle:]:
        print("YES")
    else:
        print("NO")