# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

for _ in range(int(input())):
    n = int(input())
    s = input()

    imposible_cases = 0
    min_removed_count = float("inf")
    individual_notes = set(s)

    for letter in individual_notes:
        removed_count = 0
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if s[left] == letter:
                    left += 1
                    removed_count += 1
                elif s[right] == letter:
                    right -= 1
                    removed_count += 1
                else:
                    imposible_cases += 1
                    # removed_count = float("inf")  -> I can do this to eliminate the if condition left >= right
                    break
                
        if left >= right:
            min_removed_count = min(removed_count, min_removed_count)
        
    if imposible_cases == len(individual_notes):
        print("-1")
    else:
        print(min_removed_count)
    