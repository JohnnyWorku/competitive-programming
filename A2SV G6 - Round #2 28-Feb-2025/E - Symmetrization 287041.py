# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

for _ in range(int(input())):
    n = int(input())
    matrix = []
    for _ in range(n):
        row = input()
        matrix.append(row)
        
    left = 0
    right = n - 1
    total_min_change = 0
    
    while left < right:
        top = left
        bottom = right
        
        for i in range(right - left):
            change_to_make = 0
            if matrix[top][left + i] != matrix[top + i][right]:
                change_to_make += 1
            if matrix[top][left + i] != matrix[bottom][right - i]:
                change_to_make += 1
            if matrix[top][left + i] != matrix[bottom - i][left]:
                change_to_make += 1
            
        # If change_to_make = 3 then the minimum change we want is to change matrix[top][left + i] it self 
            if change_to_make == 3:
                change_to_make = 1
            
            total_min_change += change_to_make
            
        left += 1
        right -= 1
        
    print(total_min_change)